#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Telegram bot, with a simple plugin system.
Read exampleplugin.py on more infos on how to create one.
Author(s): A Sad Loners
Last modified: June 2017
Version: 1.1
Github: https://github.com/GooogIe
"""
#Imports
from pluginHandler import PluginHandler
import sys,json,utils,os,requests,time,threading
from os.path import isfile
#Disable creation of .pyc
sys.dont_write_bytecode = True

osslash = ""

if os == 'nt':
	osslash = "\""
else:
	osslash = "/"


class Bot:
#Constructor method
	def __init__(self):
		utils.info()
		if isfile("config.vrs"):								#If there is a config load settings from there
			configs = utils.loadfile("config.vrs")
			name = configs["Name"]
			maintainer = configs["Maintainer"]
			version = configs["Version"]
			debug = configs["Debug"]
			token = configs["Token"]
		else:										            #Otherwise ask for a new token
			utils.logaction("Type the bot Token: ")
			token = raw_input("")
			utils.action("Set the Bot's Name(This is not going to change it on telegram), Version and Debug mode via CLI.")
			name = "VarasTG"
			maintainer = "A Sad Loners"
			version = "1.0"
			debug = False
		#Bot Stuff
		self.name = name
		self.maintainer = maintainer
		self.pluginHandler = PluginHandler()
		self.version = version
		self.os = os.name
		self.debug = debug
		self.token = token
		self.config = { "Name":self.name,"Maintainer":self.maintainer,"Version":self.version,"Debug":self.debug,"Token":self.token}

		#Telegram Stuff
		self.telegram_api = "https://api.telegram.org/bot" + self.token + "/"

		self.killed = []

		self.update = []
		self.update = ""
		self.update_id = ""

		self.text = ""
		self.user_id = ""
		self.username = ""
		self.first_name = ""
		self.last_name = ""

		self.chat_id = ""
		self.date = ""

		self.run = True
		self.saveConfig()

		self.pluginHandler.loadPlugins()

		#Thread to handle messages separately
		self.updatesThread = threading.Thread(target=self.getUpdates)
		self.updatesThread.setDaemon(True)
		self.updatesThread.start()

	#Defining basic methods

	def getName(self):
		return self.name

	def getVersion(self):
		return self.version

	def getDebug(self):
		return self.debug

	def setName(self,name):
		self.name = name

	def setMaintainer(self,maintainer):
		self.maintainer = maintainer

	def setVersion(self,version):
		self.version = version

	def setDebug(self,debug):
		self.debug = debug

	#Other methods
	def stopBot(self):
		self.run = False
		sys.exit()

	def startCli(self):
		#Loop to keep the bot active
		utils.action("Type help to get a list of console commands.")
		while True:
			cmd = raw_input(utils.red+'>'+utils.defcol)
			if cmd.startswith("setversion "):
				vrs = cmd.split(" ")
				self.setVersion(vrs[1])
				utils.action("Version set to "+utils.Cafe+vrs[1]+utils.defcol)
			if cmd.startswith("setname "):
				nm = cmd.split(" ")
				self.setName(nm[1])
				utils.action("Changed name to "+utils.Cafe+nm[1]+utils.defcol)
			if cmd.startswith("setmaintainer "):
				nm = cmd.split(" ")
				self.setMaintainer(nm[1])
				utils.action("Changed maintainer to "+utils.Cafe+nm[1]+utils.defcol)
			if cmd.startswith("setdebug "):
				db = cmd.split(" ")
				if db[1] == "True" or db[1] == "False":
					self.setDebug(db[1])
					utils.action("Changed Debug mode to "+utils.Cafe+db[1]+utils.defcol)
				else:
					utils.alert("Debug mode must be True or False")
			if cmd=="getname":
				utils.action("Current name is: "+utils.Cafe+self.getName()+utils.defcol)
			if cmd=="getplugins":
				utils.action("Loaded plugins are: "+utils.Cafe+self.pluginHandler.getPlugins()+utils.defcol)
			if cmd=="getversion":
				utils.action("Current version is: "+utils.Cafe+self.getVersion()+utils.defcol)
			if cmd=="getdebug":
				utils.action("Current debug mode is: "+utils.Cafe+self.getDebug()+utils.defcol)
			if cmd=="activethreads":
				utils.action("Active threads: %s" %(len(threading.enumerate())))
			if cmd=="reload":
				utils.action("Reloading "+utils.Cafe+"plugins."+utils.defcol)
				self.plugins = []
				self.pluginHandler.loadPlugins()
				utils.action("Done reloading.")
			"""if cmd=="update":
			utils.action("Attempting to update, bot will close after update.")
			utils.action("Bot will close after being updated.")
			if updater.check(ver)==True:
			utils.action("Varas is up to date!")
			else:
			updater.update()"""
			if cmd=="exit":
				self.stopBot()
			if cmd=="help":
				utils.action("Available console commands are: "+utils.Cafe+"help,activethreads,reload,setversion <version>,getversion,setname <name>,getname,setdebug <True/False>,getdebug,update,getplugins"+utils.defcol)

	#saveConfig method
	def saveConfig(self):
		utils.logaction("Saving settings to file...")
		try:
			utils.savefile("config.vrs",self.config)
			utils.action("Saved successfully to config.vrs")
		except:
			utils.alert("Failed saving settings.")

	#sendMessage method
	def sendMessage(self,text):
		return self.apiRequest("sendMessage", {'chat_id':self.chat_id, 'text':text})

	#apiRequest method, makes a request to telegram's APIs
	def apiRequest(self,method, data):
		global telegram_api
		return requests.post(self.telegram_api + method, data=data).text

	#newUpdate method
	def newUpdate(self):
		return not self.update_id in self.killed

	#getChat method
	def getChat(self):
		return self.update["message"]["chat"]

	#getUser method
	def getUser(self):
		return self.update["message"]["from"]
	#removeLastUpdate Method
	def removeLastUpdate(self):
		try:
			self.update = json.loads(self.apiRequest("getUpdates", {'offset':'-1'}))
			self.update = self.update["result"][0]
			self.update_id = self.update["update_id"]
			self.msgProcessed(self.update_id)
		except:
			utils.action("Looks like there are no updates to remove :P")
			pass


	#getUpdates method
	def getUpdates(self): #Basically the main method, keeps the bot on listening for messages
		#Keep stuff updated
		up = True
		self.removeLastUpdate()	# On startup remove last update which hasn't been parsed or the bot will send double messages to the last user
		while True:
			self.update = json.loads(self.apiRequest("getUpdates", {'offset':'-1'}))
		try:
			self.update = self.update["result"][0]
			self.update_id = self.update["update_id"]
			self.user_id = self.update["message"]["from"]["id"]
			self.username = self.update["message"]["from"]["username"]
			self.first_name = self.update["message"]["from"]["first_name"]
			self.chat_id = self.update["message"]["chat"]["id"]
			self.text = self.update["message"]["text"]
			self.date = self.update["message"]["date"]
			up = True
		except:
			if up:
				utils.alert("No updates found.")
				time.sleep(5)
				up = False
		if(self.newUpdate()):                   #If there is a new update(new message)
			if(self.text.startswith("/")):      #If the message starts with /
				self.parseMsg()
				self.msgProcessed(self.update_id)   #Add the message, whatever it was, to the processed ones so that it won't be processed again


	#Add the latest update to the processed ones
	def msgProcessed(self, u):
		self.killed.append(u)


	#Process the message received
	def parseMsg(self):
		cmd = self.text.replace("/","",1).lower()       						#Replace the / with nothing to have the pure messages text

		cmd = cmd.split(" ")                                					#Split the message by ' '
		command = cmd[0]
		if "@" in command:
			command = command.split("@")
			command = command[0]
			utils.action("User "+str(self.user_id)+"("+self.username+")"+" performed "+command+" at "+self.date)
		if self.pluginHandler.isAPlugin(command):            					#If the first element of the list is in the list of pluginf
			self.sendMessage(self.pluginHandler.runPlugin(cmd,self.getChat(),self.getUser()))     		#Call callPlugin method and send try the result
		else:                                               					#If the command isn't in the plugins list
			utils.alert("No plugin found("+command+")")

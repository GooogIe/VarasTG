#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Telegram bot, with a simple plugin system.
Read exampleplugin.py on more infos on how to create one.
Author(s): A Sad Loners
Last modified: July 2017
Version: 1.1
Github: https://github.com/GooogIe
"""
#Imports
from modules.pluginHandler import PluginHandler
from modules.telegramHandler import Telegram
from modules import logger
import sys,utils,os,threading
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
		self.info()
		if isfile("config.vrs"):								#If there is a config load settings from there
			configs = logger.loadfile("config.vrs")
			name = configs["Name"]
			maintainer = configs["Maintainer"]
			version = configs["Version"]
			debug = configs["Debug"]
			token = configs["Token"]
		else:										            #Otherwise ask for a new token
			logger.logaction("Type the bot Token: ")
			token = raw_input("")
			logger.action("Set the Bot's Name(This is not going to change it on telegram), Version and Debug mode via CLI.")
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
		self.telegramHandler = Telegram(self.token)

		self.run = True
		self.saveConfig()

		self.pluginHandler.loadPlugins()

		#Thread to handle messages separately
		self.updatesThread = threading.Thread(target=self.onUpdate)
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
	def info(self):
		logger.pinfo(logger.red+" __      __                 ")
		logger.pinfo(logger.red+" \ \    / /                 ")
		logger.pinfo(logger.red+"  \ \  / /_ _ _ __ __ _ ___ ")
		logger.pinfo(logger.red+"   \ \/ / _` | '__/ _` / __|")
		logger.pinfo(logger.red+'    \  / (_| | | | (_| \__ \ ')
		logger.pinfo(logger.red+"     \/ \__,_|_|  \__,_|___/4TG")
		logger.pinfo(logger.red+ ""+logger.defcol)
		logger.pinfo(logger.red+"Varas Telegram Bot.")
		logger.pinfo("Coded by "+logger.blue+"Neon "+logger.defcol+"and "+logger.yellow+"A Sad Loners.")
		logger.pinfo("Using "+logger.green+"Python"+logger.defcol+" 2.7.10.")
	
	def stopBot(self):
		self.run = False
		sys.exit()

	def startCli(self):
		#Loop to keep the bot active
		logger.action("Type help to get a list of console commands.")
		while True:
			cmd = raw_input(logger.red+'>'+logger.defcol)
			if cmd.startswith("setversion "):
				vrs = cmd.split(" ")
				self.setVersion(vrs[1])
				logger.action("Version set to "+logger.Cafe+vrs[1]+logger.defcol)
			if cmd.startswith("setname "):
				nm = cmd.split(" ")
				self.setName(nm[1])
				logger.action("Changed name to "+logger.Cafe+nm[1]+logger.defcol)
			if cmd.startswith("setmaintainer "):
				nm = cmd.split(" ")
				self.setMaintainer(nm[1])
				logger.action("Changed maintainer to "+logger.Cafe+nm[1]+logger.defcol)
			if cmd.startswith("setdebug "):
				db = cmd.split(" ")
				if db[1] == "True" or db[1] == "False":
					self.setDebug(db[1])
					logger.action("Changed Debug mode to "+logger.Cafe+db[1]+logger.defcol)
				else:
					logger.alert("Debug mode must be True or False")
			if cmd=="getname":
				logger.action("Current name is: "+logger.Cafe+self.getName()+logger.defcol)
			if cmd=="getplugins":
				logger.action("Loaded plugins are: "+logger.Cafe+self.pluginHandler.getPlugins()+logger.defcol)
			if cmd=="getversion":
				logger.action("Current version is: "+logger.Cafe+self.getVersion()+logger.defcol)
			if cmd=="getdebug":
				logger.action("Current debug mode is: "+logger.Cafe+self.getDebug()+logger.defcol)
			if cmd=="activethreads":
				logger.action("Active threads: %s" %(len(threading.enumerate())))
			if cmd=="reload":
				logger.action("Reloading "+logger.Cafe+"plugins."+logger.defcol)
				self.plugins = []
				self.pluginHandler.loadPlugins()
				logger.action("Done reloading.")
			"""if cmd=="update":
			logger.action("Attempting to update, bot will close after update.")
			logger.action("Bot will close after being updated.")
			if updater.check(ver)==True:
			logger.action("Varas is up to date!")
			else:
			updater.update()"""
			if cmd=="exit":
				self.stopBot()
			if cmd=="help":
				logger.action("Available console commands are: "+logger.Cafe+"help,activethreads,reload,setversion <version>,getversion,setname <name>,getname,setdebug <True/False>,getdebug,update,getplugins"+logger.defcol)

	#saveConfig method
	def saveConfig(self):
		logger.logaction("Saving settings to file...")
		try:
			logger.savefile("config.vrs",self.config)
			logger.action("Saved successfully to config.vrs")
		except:
			logger.alert("Failed saving settings.")


	def onUpdate(self):
		while self.run:
				self.parseMsg(self.telegramHandler.getUpdates())

	#Process the message received
	def parseMsg(self,text):
		cmd = text.replace("/","",1).lower()       						#Replace the / with nothing to have the pure messages text

		cmd = cmd.split(" ")                                					#Split the message by ' '
		command = cmd[0]
		if "@" in command:
			command = command.split("@")
			command = command[0]
		logger.action("User "+str(self.telegramHandler.user_id)+"("+self.telegramHandler.username+")"+" performed "+command+" at "+self.telegramHandler.date)
		if self.pluginHandler.isAPlugin(command):            					#If the first element of the list is in the list of pluginf
			self.telegramHandler.sendMessage(self.pluginHandler.runPlugin(cmd,self.telegramHandler.getChat(),self.telegramHandler.getUser(),self.telegramHandler))     		#Call callPlugin method and send try the result
		else:                                               					#If the command isn't in the plugins list
			logger.alert("No plugin found("+command+")")

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Telegram bot, with a simple plugin system.
Read exampleplugin.py on more infos on how to create one.
Author(s): Habb0n and Neon
Last modified: March 2017
Version: 1.0
Github: https://github.com/GooogIe and https://github.com/neon-loled/
"""

#Imports
from os import listdir
from os.path import isfile, join
import sys,json,utils,os,requests
osslash = ""

if os == 'nt':
		osslash = "\""
else:
		osslash = "/"

class Bot:
    #Constructor method
    def __init__(self,token, name = "Varas4Tg",version = "1.0",debug = False):
        #Bot Stuff
        self.name = name
        self.version = version
        self.plugins = []
    	self.os = os.name
    	self.debug = debug
    	self.token = token
    	self.config = { "Name":self.name,"Version":self.version,"Debug":self.debug,"Token":self.token}
        self.plugindir = os.getcwd()+osslash+"plugins"
        #Telegram Stuff
        self.telegram_api = "https://api.telegram.org/bot" + self.token + "/"
        
        self.killed = []
        
        self.update = []
        self.update = ""
        self.update_id = ""
        
        self.user_id = ""
        self.username = ""
        self.first_name = ""
        
        self.chat_id = ""
        self.text = ""
    
    #Defining basic methods

    def addPlugin(self,plugin):
        self.plugins.append(plugin)

    def getName(self):
	    return self.name

    def getVersion(self):
	    return self.version

    def getDebug(self):
	    return self.debug

    #Other methods
    
    #saveConfig method
    def saveConfig(self):
        utils.logaction("Saving settings to file...")
        try:
            utils.savefile("config.vrs",self.config)
            utils.action("Saved succesfully to config.vrs")
        except:
            utils.alert("Failed saving settings.")
    
    #getPlugins method
    def getPlugins(self):
	    return utils.Cafe+",".join(self.plugins)
        
    #sendMessage method
    def sendMessage(self,text):
        return self.apiRequest("sendMessage", {'chat_id':self.chat_id, 'text':text})
    
    #apiRequest method
    def apiRequest(self,method, data):
        global telegram_api
        return requests.post(self.telegram_api + method, data=data).text
    
    #newUpdate method
    def newUpdate(self):
        return not self.update_id in self.killed
    
    #getUpdates method
    def getUpdates(self): #Basically the main method, keeps the bot on listening for messages
        #Keep stuff updated
        while True:
            self.update = json.loads(self.apiRequest("getUpdates", {'offset':'-1'}))
            self.update = self.update["result"][0]
            self.update_id = self.update["update_id"]
            
            self.user_id = self.update["message"]["from"]["id"]
            self.username = self.update["message"]["from"]["username"]
            self.first_name = self.update["message"]["from"]["first_name"]
            
            self.chat_id = self.update["message"]["chat"]["id"]
            try:
                self.text = self.update["message"]["text"]
            except:
                pass
            
            if(self.newUpdate()):                   #If there is a new update(new message)
                if(self.text.startswith("/")):      #If the message starts with /
                    self.processMsg(self.text)      #Attempt to process it
                self.msgProcessed(self.update_id)   #Add the message, whatever it was, to the processed ones so that it won't reprocessed
    
    #Add the latest update to the processed ones
    def msgProcessed(self, u):
        self.killed.append(u)

    #Load the plugins to a list
    def loadPlugins(self):
    	for f in listdir(self.plugindir):                       #For everything in the plugins dir
    		if isfile(join(self.plugindir, f)):                 #If it's a file
    			if(f!="__init__.py" and ".pyc" not in f):       #Make sure it's not inity.py and not a bytecode files
    				f =f.replace(".py",'',1)                    #Replace the extension
    				fl = [line.strip() for line in open(self.plugindir+osslash+f+".py", 'r')]       #Load the content into a string
    				if any("def execute" and "desc =" in s for s in fl):                            #If the string contains the main function and the description
       				    if any("indexme = False" in x for x in fl):
           					utils.action("Ignored file "+utils.Cafe+f+utils.defcol+".")             #If the string contains 'indexme = False' ignore the plugin
        			    else:
           					self.addPlugin(f)                                                       #Add the plugin to the list
        					utils.action("Added "+utils.Cafe+f+utils.defcol+" plugin.")
    				else:
    					utils.alert("Couldn't add "+utils.Cafe+f+utils.defcol+" plugin, necessary functions missing(execution and/or desc).")

    #Import and execute the plugin
    def callPlugin(self,plugin):
    	exec("from plugins import "+plugin[0])             #Import the needed plugin
    	if len(plugin) ==1:                                #If the plugin has 0 parameters
    		exec("tosend = "+plugin[0]+".execute()")
    	elif len(plugin) == 2:                             #If the plugin has 1 parameter
    		exec("tosend = "+plugin[0]+".execute('"+plugin[1]+"')")
    	elif len(plugin) == 3:                             #If the plugin has 2 parameters
    		exec("tosend = "+plugin[0]+".execute('"+plugin[1]+"','"+plugin[2]+"')")
    	elif len(plugin) == 4:                             #If the plugin has 3 parameters
    		exec("tosend = "+plugin[0]+".execute('"+plugin[1]+"','"+plugin[2]+"','"+plugin[3]+"')")
    	elif len(plugin) == 5:                             #If the plugin has 4 parameters
    		exec("tosend = "+plugin[0]+".execute('"+plugin[1]+"','"+plugin[2]+"','"+plugin[3]+"','"+plugin[3]+"')")
    	return "[#] "+str(tosend)                          #Return the string to be sent
    	
    #Process the message received
    def processMsg(self,text):
        cmd = self.text.replace("/","")                     #Replace the / with nothing to have the pure messages text
    	cmd = cmd.split(" ")                                #Split the message by ' '
    	if cmd[0] in self.plugins:                          #If the first element of the list is in the list of pluginf
    		utils.action("User "+str(self.user_id)+"("+self.username+")"+" performed "+cmd[0]) 
    		if self.debug == "False":
    			try:
    				self.sendMessage(self.callPlugin(cmd))  #Call callPlugin method and send the result
    			except:                                     #Except shit not to see errors
    				utils.alert("Error while performing "+cmd[0]+" ("+self.user_id+")")
    				self.sendMessage("[#] Error while performing "+cmd[0]+" ("+self.user_id+")")
    		else:
    			self.sendMessage(self.callPlugin(cmd))      #Call callPlugin method and send try the result
    	else:                                               #If the command isn't in the plugins list
    		self.sendMessage("[#] No plugin found for "+cmd[0]+", use /help, to get a list of available commands.")
    		utils.alert("No plugin found("+cmd[0]+")")
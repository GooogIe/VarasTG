#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Plugin Handler class.
Handles every plugin and it's interactions.
Author(s): A Sad Loners
Last modified: June 2017
Github: https://github.com/GooogIe
"""
#Imports
from os import listdir
from os.path import isfile, join
import sys,json,utils,os,threading

osslash = ""

if os == 'nt':
		osslash = "\""
else:
		osslash = "/"

class PluginHandler():
    def __init__(self):
		self.plugins = []
		self.plugindir = os.getcwd()+osslash+"plugins"
		
    def addPlugin(self,name):
    	exec("from plugins import "+name)			    #Import it
        pname = None
        try:
        	exec("pname = "+name+".name")
        except NameError:
        	utils.alert(name+" is not a valid plugin, function 'getPluginName()' is missing, skipped.")
        	return
        """except:
            utils.alert("Unknown error while adding "+name)
            return"""
            
        if pname != None and pname not in self.plugins:
			exec(name +" = "+name+"."+pname+"()")
			exec("self.plugins.append("+name+")")
			utils.action(utils.Cafe+name+utils.defcol+" loaded successfully!")
        elif pname in self.plugins:
        	utils.alert(pname+" is already a plugin, skipped")
        else:
        	utils.alert("Plugin name null, skipped")

    #getPlugins method, return a string containing every plugin enabled
    def getPlugins(self):
        pls = []
        for plugin in self.plugins:
            pls.append(plugin.getName())
        if len(pls) >0:
	        return utils.Cafe+",".join(pls)
        else:
	        return ""

    def isAPlugin(self,name):
        try:
            if name in self.getPlugins():
                    return True
            return False
        except:
            return False

    #Load the plugins to a list, and make sure everything is fine in them
    def loadPlugins(self):
    	self.plugins = []
    	if not os.path.isdir(self.plugindir):
    		utils.alert("Plugins directory doesn't exists, attempting to create it.")
    		try:
				print self.plugindir
				utils.logaction("Plugins directory created successfully!")
				os.mkdir(os.getcwd()+osslash+"plugins")
    		except:
    			utils.errorquit("Couldn't create plugins directory...quitting.")
        for f in listdir(self.plugindir):                       #For every item in the plugins dir
        	if isfile(join(self.plugindir, f)):                 #If it's a file
        		if(f!="__init__.py" and ".pyc" not in f and f!="plugin.py"):       #Make sure it's not init.py and not a bytecode files
					f =f.replace(".py",'',1)                    #Clear the .py from the name
					self.addPlugin(f)							#Run addPlugin(plugin)
        utils.action("Loaded "+str(len(self.plugins))+" plugins.")

    def runPlugin(self,args,chat,user):
        name = args[0]
        args.pop(0)
        for plugin in self.plugins:
            if plugin.getName() == name:
                try:
                    plugin.setInfo(chat,user)
                    return plugin.run(*args)
                except TypeError:
                	return "Invalid number of parameters specified."

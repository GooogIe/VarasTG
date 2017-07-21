#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Help plugin for Varas
Author: Habb0n
Last modified: June 2017
"""

from plugin import Plugin
import os
from os import listdir
from os.path import isfile, join

name = 'Help'
    
if os.name == "nt":
    osslash = "\""
else:
    osslash = "/"

plugindir = os.getcwd()+osslash+"plugins"
    
class Help(Plugin):
    def __init__(self):
        Plugin.__init__(self,"help","Shows a list of the commands.","A Sad Loners",1.0)
    
    def run(self):
    	help= [f for f in listdir(plugindir) if isfile(join(plugindir, f))]		        #Load plugins dir content into a list
    	i = 0
    	while i < len(help):
    		if ".pyc" in help[i] or "__init__" in help[i] or "plugin" in help[i]:		#If .pyc or __init__ in filename
    			del help[i]							                                    #Delete it from plugins list
    		else:
    			help[i] = help[i].replace(".py","")			                            #Replace extension
    			pname = pluginname = ""
    			if help[i] != "help":						                            #If it's not help
    				exec("import "+help[i])				                                #Import
    				exec("pname = "+help[i]+".name")
    				exec("obj = "+help[i]+"."+pname+"()")
    				exec("dc = obj.getDesc()")				                            #Get description
    				exec("pluginname = obj.getName()")
    			else:
    				dc = self.desc
    				pluginname = "help"
    			help[i] = "/"+pluginname+" - "+dc					                            #Edit plugin with this format: "name - description"
    			i +=1
    	help.sort()									                                    #Sort plugin list
    	return "Available commands: \n"+"\n".join(help)					                #Return the string
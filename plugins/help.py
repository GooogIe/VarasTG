#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Help plugin for Varas
Author: Habb0n
Last modified: March 2017
"""

import os
from os import listdir
from os.path import isfile, join

desc = "Simple command that let you see all the bot plugins."

osslash = ""

if os.name == "nt":
	osslash = "\""
else:
	osslash = "/"

plugindir = os.getcwd()+osslash+"plugins"

def execute():
	help= [f for f in listdir(plugindir) if isfile(join(plugindir, f))]		   #Load plugins dir content into a list
	i = 0
	while i < len(help):
		fl = [line.strip() for line in open(plugindir+osslash+help[i], 'r')]       #Load the content into a string
		if ".pyc" in help[i] or "__init__" in help[i]:			           #If .pyc or __init__ in filename
			del help[i]							   #Delete it from plugins list
		elif any("indexme = "+"False" in x for x in fl):			   #Check if it contains indexme = False
			del help[i]							   #If yes delete if from plugins list
		else:
			help[i] = help[i].replace(".py","")			           #Replace extension
			if help[i] != "help":						   #If it's not help
				exec("import "+help[i])				           #Import
				exec("dc = "+help[i]+".desc")				   #Get description
			else:
				dc = desc
			help[i] = help[i]+" - "+dc					   #Edit plugin with this format: "name - description"
			i +=1
	help.sort()									   #Sort plugin list
	return "Available commands: \n"+"\n".join(help)					   #Return the string
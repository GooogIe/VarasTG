#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Utils module for Varas
Author: A Sad Loners
Last modified: March 2017
"""

import json
import sys
import requests
#Colors
white="\033[1;37m"
grey="\033[0;37m"
purple="\033[0;35m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
purple="\033[0;35m"
cyan="\033[0;36m"
Cafe="\033[0;33m"
fucsya="\033[1;35m"
blue="\033[1;34m"
transparent="\e[0m"
defcol = "\033[0m"

#Don't write bytecodes file (.pyc)
sys.dont_write_bytecode = True

#Useful function
def savefile(fltsave,cont):
	json.dump(cont, open(fltsave,'w+'))

def loadfile(fltload):
	conf = json.load(open(fltload))
	return conf

#Print functions
def logaction(text):
	print red+"["+blue+"#"+red+"] - "+defcol+text

def action(text):
	print red+"["+green+"+"+red+"] - "+defcol+text

def alert(text):
	print red+"["+yellow+"!"+red+"] - "+defcol+text

def pinfo(text):
	print red+"["+blue+"@"+red+"] - "+defcol+text

def errorquit(text):
	print red+"["+purple+"-"+red+"] - "+defcol+text
	raw_input('\nPress the <ENTER> key to EXIT...')
    	sys.exit()

def info():
	pinfo(red+" __      __                 ")
	pinfo(red+" \ \    / /                 ")
	pinfo(red+"  \ \  / /_ _ _ __ __ _ ___ ")
	pinfo(red+"   \ \/ / _` | '__/ _` / __|")
	pinfo(red+'    \  / (_| | | | (_| \__ \ ')
	pinfo(red+"     \/ \__,_|_|  \__,_|___/4TG")
	pinfo( ""+defcol)
	pinfo(red+"Varas Telegram Bot.")
	pinfo("Coded by "+blue+"Neon "+defcol+"and "+yellow+"Gooogle.")
	pinfo("Using "+green+"Python"+defcol+" 2.7.10.")

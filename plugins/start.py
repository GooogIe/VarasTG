#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
start plugin for Varas
Author: A Sad Loners
Last modified: June 2017
"""

import urllib2
from plugin import Plugin

name = 'Start'

    
class Start(Plugin):
    def __init__(self):
        Plugin.__init__(self,"start","Start the bot.","A Sad Loners",1.0)
    
    def run(self):
    	return "Welcome on my Bot "+self.user["first_name"]+"\nUse /help to get a list of available commands.\nPowered By VarasTg - https://github.com/GooogIe/VarasTG\nWritten in Python by @eigoog"

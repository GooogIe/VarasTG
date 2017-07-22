#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Chat plugin for Varas
Author: A Sad Loners
Last modified: June 2017
"""

import urllib2
from plugin import Plugin

name = 'Chat'

    
class Chat(Plugin):
    def __init__(self):
        Plugin.__init__(self,"chat","Returns a list of informations about che current chat.","A Sad Loners",1.0)
    
    def run(self):
		infos = "Hi "+self.user["first_name"]+" these are some chat's informations:\n"
		infos += "Id: "+str(self.chat["id"])+"\n"
		if self.chat["type"] == "group":
			infos += "Title: "+self.chat["title"]+"\n"
			infos += "Type: Group\n"
			if self.chat["all_members_are_administrators"]:
				infos += "Administrators: Everyone"
			else:
				infos += "Administrators"
		elif self.chat["type"] == "supergroup":
			infos += "Title: "+self.chat["title"]+"\n"
			infos += "Type: Supergroup\n"
		elif self.chat["type"] == "private":
			infos += "Username: "+self.chat["username"]+"\n"
			infos += "Type: Private"
		return infos

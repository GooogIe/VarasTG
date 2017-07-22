#!/usr/bin/python
# -*- coding: utf-8 -*-

#This attribute is ESSENTIAL for a plugin, as it represent the class name.
name = None

"""
This class is intended to be a guideline for every other plugin,
every plugin inherit it's structure from this one.
Author(s): A Sad Loners
Last modified: July 2017
Github: https://github.com/GooogIe and https://github.com/neon-loled/
"""

class Plugin(object):
    def __init__(self,name,desc,version,author):
        # Static stuff
        self.name = name    # Plugin Name
        self.desc = desc    # Plugin Description
        self.version = version # Plugin version
        self.author = author  # Plugin author
    
        # Used runtime
        self.user = None    # Dictionary containing all user's infos
        self.chat = None    # Dictionary containing all chat's infos
        self.telegram = None # Object used to handle telegram's requests and stuff

    # Need to be redefined
    def run(self):
        raise NotImplementedError

    # Do not edit this function unless you don't need it specifically - Not necessary
    def setInfo(self,user,chat,telegram):
        self.user = user
        self.chat = chat
        self.telegram = telegram
    # Redefine the following methods as you prefer - Not necessary
    def getVersion(self):
        return str(self.version)

    def getDesc(self):
        return self.desc

    def getAuthor(self):
        return self.author

    def getName(self):
        return self.name

    def sendMessage(self,text):
        return self.telegram.apiRequest("sendMessage", {'chat_id':self.chat["id"], 'text':text})

    def about(self):
        return "Version: "+str(self.version)+"\nDescription: "+self.desc+"\nAuthor: "+self.author

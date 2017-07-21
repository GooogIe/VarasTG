#!/usr/bin/python
# -*- coding: utf-8 -*-

#This attribute is ESSENTIAL for a plugin, as it represent the class name.
name = None

"""
This class is intended to be a guideline for every other plugin,
every plugin inherit it's structure from this one.
Author(s): A Sad Loners
Last modified: June 2017
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

    # Need to be redefined
    def run(self):
        raise NotImplementedError

    # Do not edit this function unless you don't need it specifically - Not necessary
    def setInfo(self,chat,user):
        self.user = user
        self.chat = chat

    # Redefine the following methods as you prefer - Not necessary
    def getVersion(self):
        return str(self.version)

    def getDesc(self):
        return self.desc

    def getAuthor(self):
        return self.author

    def getName(self):
        return self.name

    def about(self):
        return "Version: "+str(self.version)+"\nDescription: "+self.desc+"\nAuthor: "+self.author

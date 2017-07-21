#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Isup plugin for Varas
Author: Neon & A Sad Loners
Last modified: June 2017
"""

import urllib2
from plugin import Plugin

name = 'Isup'

    
class Isup(Plugin):
    def __init__(self):
        Plugin.__init__(self,"isup","<url> Check if a website is up or not","A Sad Loners",1.0)
    
    def run(self,url):
    	api = urllib2.urlopen("http://isup.me/"+url)
    	read = api.read()
    	
    	if "It's not just you!" in read:
    		return url + " is offline."
    	elif "It's just you" in read:
    		return url+ " is online."
    	else:
    		return "An error has occured."
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Geoip plugin for Varas
Author: Neon & A Sad Loners
Last modified: June 2017
"""

import urllib2
from plugin import Plugin

name = 'Geoip'

    
class Geoip(Plugin):
    def __init__(self):
        Plugin.__init__(self,"geoip","<ip> Attempt to retrieve infos about a provided IP","A Sad Loners",1.0)
    
    def run(self,ip):
	try:
	    	api = urllib2.urlopen("http://api.predator.wtf/geoip/?arguments="+ip)
	    	read = api.read()
	    	rtr = read.replace("<br>", "\n",100)
	    	return rtr
	except:
		return "Error while executing geoip of %s" % (ip)

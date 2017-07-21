#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Btc plugin for Varas
Author: Neon & A Sad Loner
Last modified: November 2016
"""

import urllib2
from plugin import Plugin

name = 'Bitcoin'

    
class Bitcoin(Plugin):
    def __init__(self):
        Plugin.__init__(self,"bitcoin","<wallet> Return current balance from a Bitcoin wallet","A Sad Loners",1.0)
    
    def run(self,address):
    	#1btc = 100000000satoshi
    	print "https://blockchain.info/it/q/addressbalance/"+address
    	try:
    	    api = urllib2.urlopen("https://blockchain.info/it/q/addressbalance/"+address)
    	except:
    	    return "Unknown Error"
    	resp = api.read()
    	
    	satoshi = float(resp)
    	btc = satoshi/100000000
    	
    	return "Balance: " + str(btc)
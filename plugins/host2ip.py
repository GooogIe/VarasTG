#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Host2ip plugin for Varas
Author: A Sad Loners
Last modified: June 2017
"""

import socket
from plugin import Plugin

name = 'Host2ip'

    
class Host2ip(Plugin):
    def __init__(self):
        Plugin.__init__(self,"host2ip","<hostname> Retrieve the IP address from an hostname.","A Sad Loners",1.0)
    
    def run(self,url):
    	return str(url+ "'s IP: "+socket.gethostbyname(url))
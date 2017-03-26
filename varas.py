#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Telegram bot, with a simple plugin system.
Read exampleplugin.py on more infos on how to create one.
Author(s): Habb0n and Neon
Last modified: March 2017
Version: 1.0
Github: https://github.com/GooogIe and https://github.com/neon-loled/
"""

import bot,utils
from os.path import isfile


def main():
    											#Initializing bot instance
    if isfile("config.vrs"):								#If there is a config load settings from there
        configs = utils.loadfile("config.vrs")
        name = configs["Name"]
        version = configs["Version"]
        debug = configs["Debug"]
        token = configs["Token"]
        myBot = bot.Bot(token,name,version,debug)
    else:										#Otherwise ask for a new token
    	utils.logaction("Type the bot Token: ")
    	token = raw_input("")
    	varas = bot.Bot(token)
        
    utils.info()
    varas.saveConfig()
    varas.loadPlugins()
    varas.getUpdates()
    
if __name__ == "__main__":
	main()

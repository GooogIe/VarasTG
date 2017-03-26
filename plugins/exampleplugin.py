#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Example plugin for Vars
Author: Habb0n
Last modified: March 2017
Github: https://github.com/GooogIe
"""

desc = "A simple description about what your command will do" # The description it is NECESSARY or plugin won't be loaded

indexme = False                                               # Add this line if you don't want this file to be loaded as plugin

def execute(num1,num2): #This is the essence of the plugin, it must have this function and it must return something or the bot will not load it
	#For example i wanna calculate the sum of the two number given in input
	return num1+num2 #And this will return to the program the value of num1+num2

#You can even create other function and recall it in the execute function.
#This bot is still a beta and it has a lot of bugs, we accomplish for any issue, and you can help us by making us notice it, thank you -Devs
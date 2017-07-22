#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Little telegram module to interact with it's API
Author(s): A Sad Loners
Last modified: July 2017
Version: 1.1
Github: https://github.com/GooogIe
"""

import requests,json,logger,time

class Telegram():
    #Constructor method
	def __init__(self,token):
		#Telegram Stuff
		self.token = token
		self.telegram_api = "https://api.telegram.org/bot" + self.token + "/"

		self.killed = []

		self.update = []
		self.update = ""
		self.update_id = ""

		self.text = ""
		self.user_id = ""
		self.username = ""
		self.first_name = ""
		self.last_name = ""

		self.chat_id = ""
		self.date = ""
		
	#sendMessage method
	def sendMessage(self,text):
		return self.apiRequest("sendMessage", {'chat_id':self.chat_id, 'text':text})

	#apiRequest method, makes a request to telegram's APIs
	def apiRequest(self,method, data):
		global telegram_api
		return requests.post(self.telegram_api + method, data=data).text

	#newUpdate method
	def newUpdate(self):
		return not self.update_id in self.killed

	#getChat method
	def getChat(self):
		return self.update["message"]["chat"]

	#getUser method
	def getUser(self):
		return self.update["message"]["from"]
	#removeLastUpdate Method
	def removeLastUpdate(self):
		try:
			self.update = json.loads(self.apiRequest("getUpdates", {'offset':'-1'}))
			self.update = self.update["result"][0]
			self.update_id = self.update["update_id"]
			self.msgProcessed(self.update_id)
		except:
			logger.action("Looks like there are no updates to remove :P")
			pass
			
	#Add the latest update to the processed ones
	def msgProcessed(self, u):
		self.killed.append(u)



	#getUpdates method
	def getUpdates(self): #Basically the main method, keeps the bot on listening for messages
		#Keep stuff updated
		up = True
		self.removeLastUpdate()	# On startup remove last update which hasn't been parsed or the bot will send double messages to the last user
		while True:
			self.update = json.loads(self.apiRequest("getUpdates", {'offset':'-1'}))
			try:
				self.update = self.update["result"][0]
				self.update_id = self.update["update_id"]
				self.user_id = self.update["message"]["from"]["id"]
				self.username = self.update["message"]["from"]["username"]
				self.first_name = self.update["message"]["from"]["first_name"]
				self.chat_id = self.update["message"]["chat"]["id"]
				self.text = self.update["message"]["text"]
				self.date = time.strftime("%B %d %Y", self.update["message"]["date"])
				up = True
			except:
				if up:
					logger.alert("No updates found.")
					time.sleep(5)
					up = False
			if(self.newUpdate()):                   #If there is a new update(new message)
				if(self.text.startswith("/")):      #If the message starts with /
					self.msgProcessed(self.update_id)   #Add the message, whatever it was, to the processed ones so that it won't be processed again
					return self.text

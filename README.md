# VarasTG
Varas Bot rewritten to suit for the Telegram Messaging Platform

# What is  Varas

#### Varas is a simple Telegram bot with a plugin system written in Python.

<p align="center"><img src="http://i.imgur.com/jvQrRAK.png" /></p><br>

# Running Varas on Linux

### Requirements 

* Python installed on your computer (Under Python3)
* A telegram bot (Create one through @BotFather)
* Dependencies: requests,json (Almost always installed by default)
* Brain

#### Once moved to the directory where you cloned the repo with the terminal just type:
* Take note of the bot's token you've created
* Run the bot by issuing: "python varas.py"
* Paste the token and enter
* And you're ready to go

## Creating a Plugin

* First step move to the /plugins directory.
* Create a new file whose extension will be .py
* Open it and define a description:
```python
desc = "The description of the plugin."
```
* Once you're done with the description create the execution function:
```python
def execute():
  return "Hello World."
  #This will make the bot send 'Hello World.' on the chat you've typed the command.
```
* You can also pass up to 4 parameters to the function:
```python
def execute(one,two,three,four):
  return one+two+three+four
  #This will make the bot send 'the sum of the 4 parameters in the chat you've typed the command
```

* For further examples look at the help.py plugin and exampleplugin.py [here](https://github.com/GooogIe/Varas/tree/master/Plugins)

***
# More #

### Contributors:

* Neon/Loled

### You can find me on:

* [Holeboards](http://www.holeboards.eu/User-u0qq%C9%90H)
* [Telegram](http://www.telegram.me/elgoog)

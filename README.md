# VarasTG
Varas Bot rewritten to suit for the Telegram Messaging Platform

# What is  Varas

#### Varas is a simple Telegram bot with a plugin system written in Python.

<p align="center"><img src="http://imgur.com/sMrgjaXl.png" /></p><br>

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
* If you will skip ANY of these steps your plugin won't work

* Open it and import the plugin structure by typing:
```python
from plugin import Plugin
```
* Now define a name for the plugin:
```python
name = "PluginName"
```
* Create a class and name it as you prefer(usually the plugin name will fit):
```python
class PluginName(Plugin):
```
* Define the init method, and initialize your plugin here:
```python
    def __init__(self):
        Plugin.__init__(self,"PluginName","Description","Author",1.0)
```
* Finally define the run function which is the one executed when the plugin is ran:
```python
    def run(self):
      return "Hello this is my first plugin!"
```

* Use the "self.chat" and "self.user" dictionaries to access user's and chat infos, look at the chat plugin for more.

* For further examples look at the help.py plugin and the others [here](https://github.com/GooogIe/Varas/tree/master/Plugins)

***
# More #

### Contributors:

* Neon/Loled

### You can find me on:
* [Telegram](http://www.telegram.me/elgoog)

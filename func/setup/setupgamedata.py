#!/bin/python
''' 
Structure of game data variable

player:
    name [str]
    health [int]
    statuseffects [arr]
    deck [arr]:
        card1 [str]
        card2 [str]
        ...
    

bot:
    name [str]
    health [int]
    statuseffects [arr]
    deck [arr]: 
        card1 [str]
        card2 [str]
        ...

board:
    player:
        playingcards [dict]:
            card1:
                card [str]
                position [int]
            card2:
                card [str]
                position [int]
            ...data:dict
            card2:
                card [str]
                position [int]
            ...
'''
def setup(playerdeck:list, botdeck:list, settings:dict) -> dict: # Args: Main Game Data, the players full deck, and the bots full deck
    data = {}
   
    #? set up base categories
    data["player"] = {}
    data["bot"] = {}
    data["board"] = {}

    #? set up player level 2
    data["player"]["name"] = settings["playerName"]
    data["player"]["health"] = settings["playerBaseHealth"]
    data["player"]["statuseffects"] = []
    data["player"]["deck"] = playerdeck

    #? set up bot level 2
    data["bot"]["name"] = settings["botName"]
    data["bot"]["health"] = settings["botBaseHealth"]
    data["bot"]["statuseffects"] = []
    data["bot"]["deck"] = botdeck

    #? set up board level 2
    data["board"]["player"] = {}
    data["board"]["bot"] = {}

    #? set up board level 3
    data["board"]["player"] = {}
    data["board"]["bot"] = {}

    #? set up board level 4
    data["board"]["player"]["playingcards"]  = {}
    data["board"]["bot"]["playingcards"] = {}


    return data
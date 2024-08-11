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
            ...
    
    bot:
        playingcards [dict]:
            card1:
                card [str]
                position [int]
            card2:
                card [str]
                position [int]
            ...
'''
def setup(data:dict, playerdeck:arr, botdeck:arr) -> dict:
    #? set up base categories
    data["player"] = {}
    data["bot"] = {}
    data["board"] = {}

    #? set up player level 2
    data["player"]["name"] = ""
    data["player"]["health"] = ""
    data["player"]["statuseffects"] = []
    data["player"]["deck"] = playerdeck

    #? set up bot level 2
    data["bot"]["name"] = ""
    data["bot"]["health"] = ""
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
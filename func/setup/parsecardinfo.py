#!/bin/python
import os
import json

'''
parseCards:
    get all the possible cards

    card structure:
        - Name
        - Use function(s):
            This is going to list whatever code the card will run when played that does a certain action (modify a certain variable, etc)
        - Defend function(s):
            This is going to list whatever code the card will run when played as a reaction to another card that does a certain action
        - Sacrifice function(s):
            This is going to list whatever code the card will run when it is sacrificed
        
'''
def parseCards() -> dict:
    cards = {}

    for file in os.listdir('./data/cards/defense'):
        with open(f'./data/cards/defense/{file}') as f:
            cardInfo = json.load(f)

            cards[cardInfo["name"]] = cardInfo 
            cards[cardInfo["name"]]["category"] = "defense"
    
    for file in os.listdir('./data/cards/offense'):
        with open(f'./data/cards/offense/{file}') as f:
            cardInfo = json.load(f) 

            cards[cardInfo["name"]] = cardInfo 
            cards[cardInfo["name"]]["category"] = "offense"
    
    for file in os.listdir('./data/cards/utility'):
        with open(f'./data/cards/utility/{file}') as f:
            cardInfo = json.load(f) 

            cards[cardInfo["name"]] = cardInfo
            cards[cardInfo["name"]]["category"] = "utility"
    
    return cards
        

        
#!/bin/python
import os
import importlib
import func.logging.logerror as logerror


'''
CardHandler:
    A way to process using cards
'''
class CardHandler():

    def __init__(self, cards):
        self.cards = cards

    def runFunc(self, functionName):
        for file in os.listdir('./func/cards/functions'):
            if file == "__pycache__": continue 

            func = importlib.import_module(f'func.cards.functions.{file[:-3]}').CardFunction()

            if func.functionName == functionName:
                func.run()
    
    def processCardUse(self, cardName):
        if cardName not in list(self.cards): logerror(title="Card Requested not in Cards"); raise Exception("Card Requested not in Cards")

        for function in self.cards[cardName]["useFunctions"]:
            self.runFunc(function)
    
    def processCardDefend(self, cardName):
        if cardName not in list(self.cards): logerror(title="Card Requested not in Cards"); raise Exception("Card Requested not in Cards")

        for function in self.cards[cardName]["defendFunctions"]:
            self.runFunc(function) 
    
    def processCardSacrifice(self, cardName):
        if cardName not in list(self.cards): logerror(title="Card Requested not in Cards"); raise Exception("Card Requested not in Cards")

        for function in self.cards[cardName]["sacrificeFunctions"]:
            self.runFunc(function) 


        

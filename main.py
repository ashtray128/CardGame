#!/bin/python
'''
main.py:
    Main file
    Should only be calling functions (except for the bit of code to import all the functions)
    Handles data transfer between functions

'''

#* PUBLIC LIBRARIES ------------------------------------------------------------------
import os
import sys
from colorama import Fore

#* IMPORTING OTHER PROJECT FILES ------------------------------------------------------------------
import func.logging.resetlogs as resetlogs
import func.logging.logerror as logerror

import func.setup.getinfo as getinfo 
import func.setup.parsecardinfo as parsecardinfo 
import func.setup.parsesettings as parsesettings 
import func.setup.setupgamedata as setupgamedata 

import func.display.display as display

import func.cards.cardfunctions as cardfunctions


#* CODE ------------------------------------------------------------------
def main():
    #? reset logs from previous run
    resetlogs.resetLogs()

    #? get the settings
    settings = parsesettings.parseSettings()

    #? get and parse the decks
    playerDeck = getinfo.getDeck(1)

    botDeck = getinfo.getDeck(2)

    #? create basic game data
    gameData = setupgamedata.setup(playerDeck, botDeck, settings)

    #? create card data
    cards = parsecardinfo.parseCards()

    #? set up card handler
    cardHandler = cardfunctions.CardHandler(cards)

if __name__ == "__main__":
    main()
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

#* IMPORTING OTHER PROJECT FILES ------------------------------------------------------------------
imports = []
def listfiles(path='.'):
    for entry in os.listdir(path):
        if "__pycache__" in entry: continue 
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            listfiles(full_path)
        else: 
            print(full_path)


sys.exit()


#* IMPORTANT VARIABLES ------------------------------------------------------------------

# this is what holds all the important game data like current deck, health, wtv
gameData:dict = {}

#* CODE ------------------------------------------------------------------
#? reset logs from previous run
resetlogs.resetLogs()

#? create basic game data
#gameData = setup.setupgamedata.setup()
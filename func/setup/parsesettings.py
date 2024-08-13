#!/bin/python 
import json

'''
getConfig:
    functions for parsing the games settings
    The title section in the settings is for when I eventually make a menu where you can edit settings so it doesn't look like code settings, however isn't needed for parsing the settings and would just cause more confusion
    #TODO: Make settings editor
'''
def parseSettings() -> dict:
    settings = {}

    with open('./data/settings.json', 'r') as f:

        basesettings = json.load(f)

        for setting in basesettings:
            settings[setting] = basesettings[setting]['value']
    
    return settings


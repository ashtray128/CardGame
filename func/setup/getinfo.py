#/bin/python
import json

''' 
getDeck:
    returns the deck of the specified side
    side 1: player
    side 2: bot
'''
def getDeck(side:int) -> list:
    with open('./data/deck.json', 'r') as f:
        try: deckDict = json.load(f)
        except Exception as e: getDeckErrorChecking(error=1, exception=e)
    
    if side == 1:
        if not isinstance(deckDict["player"], list):
            raise Exception("Deck isn't an array")
        return deckDict["player"]
    elif side == 2:
        return deckDict["bot"]
    else:
        return deckDict["player"]
        
'''
getDeckErrorChecking
    checks for future errors, so I can handle them how I want
    error codes:
        1 - Error when doing json.load of the deck file
'''
def getDeckErrorChecking(side:int=None, deckDict:dict=None, error:int=None, exception=None): 

    if error is not None:
        if error == 1:
            if exception is not None: logging.logerror.log(title="Failure loading deck data",text=e)
            raise Exeption("Failure loading deck data")



    if side not in [1, 2] and side is not None:
        raise Exception("Requested invalid deck")
    
    if not isinstance(deckDict, dict) and deckDict is not None: #TODO: Make this be handled automatically by resetting deck config to a backup of the base one? Have the current one be saved in backup incase of changes during use.
        raise Exception("Deck data isn't a dictionary")

    if not isinstance(deckDict["player"], list) and deckDict is not None:
        raise Exception("Player deck isn't an array")
    
    if not isinstance(deckDict["bot"], list) and deckDict is not None:
        raise Exception("Bot deck isn't an array")
    
    
    
    

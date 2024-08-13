#/bin/python
import json
import func.logging.logerror as logerror

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
    
    getDeckErrorChecking(side, deckDict)

    if side == 1:
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
            if exception is not None: logerror.log(title="Failure loading deck data",text=exception)
            else: logerror.log(title="Failure loading deck data")
            raise Exception("Failure loading deck data")



    if side not in [1, 2] and side is not None:
        logerror.log(title="Requested invalid deck")
        raise Exception("Requested invalid deck")
    
    if not isinstance(deckDict, dict) and deckDict is not None: #TODO: Make this be handled automatically by resetting deck config to a backup of the base one? Have the current one be saved in backup incase of changes during use.
        logerror.log(title="Deck data isn't a dictionary")
        raise Exception("Deck data isn't a dictionary")

    if not isinstance(deckDict["player"], list) and deckDict is not None:
        logerror.log(title="Deck data isn't a dictionary")
        raise Exception("Player deck isn't an array")
    
    if not isinstance(deckDict["bot"], list) and deckDict is not None:
        logerror.log(title="Bot deck isn't an array")
        raise Exception("Bot deck isn't an array")
    
    
    
    

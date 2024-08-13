#/bin/python
import datetime
from colorama import Fore
import pytz 

''' 
log
    Logs an error to the errors.txt file 
    doesn't really need much explanation

    Format: 

    " 

    <MM/DD/YYYY HH:MM A/PM>

    Title:
    <error title>

    Text:
    <error text>

    ----------------------------------------------------------------------
    "
'''
def log(title:str,text:str=None):
    output = ""

    output += "----------------------------------------------------------------------"

    output += "\n"

    output += datetime.datetime.now(pytz.timezone("US/Eastern")).astimezone().strftime("%m/%d/%Y %I:%M %p")

    output += "\nTitle: "

    output += title

    output += "\n"

    if text is not None:
        output += "Text: "

        output += str(text) 

        output += "\n"

    with open('./data/logs/errors.txt', 'a') as f:
        f.write(output)
    
    with open('./data/logs/total.txt', 'a') as f:
        f.write(output)
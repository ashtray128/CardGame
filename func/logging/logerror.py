#/bin/python
import datetime
from colorama import Fore

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

    output += Fore.RED

    output += "\n"

    output += datetime.datetime.now(datetime.timezone.est).astimezone().strftime("%m/%d/%Y %I:%M %p")

    output += "Title:"

    output += title

    output += "\n"

    if text is not None:
        output += "Text:"

        output += text 

        output += "\n"
    
    output += "----------------------------------------------------------------------"

    with open('./data/logs/errors.txt', 'a') as f:
        f.write(output)
    
    with open('./data/logs/total.txt', 'a') as f:
        f.write(output)
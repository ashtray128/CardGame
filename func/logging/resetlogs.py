#/bin/python
import os

''' 
resetLogs:
    Resets all the log files
    #TODO: Use for when restarting program for now, get rid of when save data persists

'''
def resetLogs():
    for log in os.listdir('./data/logs'):
        print(log)
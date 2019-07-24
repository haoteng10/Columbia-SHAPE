# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:49:41 2019

@author: ht2531
"""

#Using State Machine to find a string

def findingSubString(secretMessage, inputMessage):
    inputMessage = str(inputMessage)
    done = False
    currentState = 0
    totalState = len(secretMessage)-1
    inputMessagePosition = 0
    secretMessagePosition = 0
    times = 0
    
    while (done != True):
        if (currentState < totalState and inputMessagePosition < len(inputMessage)):
            if (inputMessage[inputMessagePosition] == secretMessage[secretMessagePosition]):
                currentState += 1
                secretMessagePosition += 1
            
            else:
                currentState = 0
            inputMessagePosition += 1
        elif (secretMessagePosition == len(secretMessage) -1):
            print("Reached")
            times += 1
            secretMessagePosition = 0
            if (inputMessage[inputMessagePosition] == secretMessage[secretMessagePosition]):
                secretMessagePosition = secretMessage/2 
                currentState = currentState / 2
        else:
            if (secretMessagePosition == len(secretMessage) -1):
                times += 1
            done = True
    return times
        
print(findingSubString("mama", "mamamama"))

        

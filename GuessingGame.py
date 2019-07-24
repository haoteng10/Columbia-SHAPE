# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:20:13 2019

@author: ht2531
"""
import random

secretNumber = int(random.random() * 11)
correctChoice = False

while(correctChoice != True):
    userNumber = int(input("Take a guess: "))
    if(userNumber == secretNumber):
        correctChoice = True
        print("You got it!")
    else:
        if(secretNumber > userNumber):
            dif = secretNumber - userNumber
        else:
            dif = userNumber - secretNumber
            
        print("The difference is " + str(dif))
        if(dif > 5):
            print("Not even close!")
        elif(dif >= 3 and dif <= 5):
            print("close!")
        else:
            print("Almost there!")
    


# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:11:38 2019

@author: ht2531
"""

#--------------Decimal to Binary Convertor------------------
    
#11 --> 
    
#11%2 5 1
#5%2 1
#2%2 0
#1%2 1

#1011
userInput = int(input("Choose a number:"))
gotZero = False
result = ""

while(gotZero==False):
    result = result + str(userInput % 2)
    if(userInput<=1):
        gotZero = True
    else:
        userInput = userInput // 2

counter = len(result) -1
reversedString = ""
while(counter>=0):
    reversedString = reversedString + result[counter]
    counter = counter - 1

print(reversedString)


#-------------Binary to Decimal Convertor---------------------------

#11 --> 1 --> ""
#-->1+2

inputBinary = input("Please enter the binary:")
index=len(inputBinary)-1
val = 1
result = 0

while(index>=0):
    if inputBinary[index] == "1":
        result = result + val
    index-= 1
    val= val * 2

print(result)
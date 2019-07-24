# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:00:07 2019

@author: ht2531
"""

print("Hello ENGIE0002! \n")
5+2
5%2
5//2
2**5

#--------------Question 6---------------

print("My name is " + "Hao. " + "My age is " + str(15) + ".\n")

#--------------Question 7------------------------

man = 1
wives = 7 * man
sacks = 7 * wives
cats = 7 * sacks
kittens =7 * cats

print("There are " + str(man) + " man. \r")
print("There are " + str(wives) + " wives. \r")
print("There are " + str(sacks) + " sacks. \r")
print("There are " + str(cats) + " cats. \r")
print("There are " + str(kittens) + " Kittens. \r")

#----------------Question 8--------------------------------
#Research

#---------------Question 9-----------------------------------

print("")

row = 5
column = 7
for i in range(row):
    for x in range(column):
        print("*", end = '')
    print("\r")
    
#----------------Question 10------------------------------------
    
inputName = input("What is your name?")
inputAge = int(input("What is your age?"))

print("Your name is " + inputName + " and your age is " + str(inputAge))


#---------------Question 11-----------------------------------

inputSeconds = int(input("Enter in seconds: "))

#Convert to minutes

initialMinutes = inputSeconds // 60
seconds = inputSeconds % 60

#Convert to hour

finalHour = initialMinutes // 60
finalMinutes = initialMinutes % 60

print(str(finalHour) + " hour(s) "+ str(finalMinutes) + " minute(s) " + str(seconds) + " second(s)")

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

inputBinary = int(input("Please enter the binary:"))
index=len(inputBinary)-1
val = 1
result = 0

while(index>0):
    if inputBinary[index] == "1":
        result = result + val
    index-= 1
    val*= 2
    
print (result)

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:46:06 2019

@author: ht2531
"""

#Question 1 (Research)

#Question 2
#not a or (b or not (a and b))

#if a is false --> everything is true

#if a is true & b is true....it is true
# if a is true & b is false....it is true

#Question 3
check_value = int(input("Value that you want to check: "))
if (check_value > 0):
    print("It is  a postive value.")
elif (check_value == 0):
    print("Null")
else:
    print("It is a negative value.")

#Question 4

#Max & Min

valueOne = int(input("First integer value: "))
valueTwo = int(input("Second integer value: "))

if(valueOne > 0 and valueTwo > 0):
    if(valueOne > valueTwo):
        minValue = valueTwo - valueOne
    else:
        minValue = valueOne - valueTwo
    maxValue = valueOne + valueTwo
else:
    if(valueOne > valueTwo):
        maxValue = valueOne - valueTwo
    else:
        maxValue = valueTwo - valueOne
    minValue = valueOne + valueTwo
    
print("The minimum is: " + str(minValue) + ", and the maximum is: " + str(maxValue))

#Question 5
#Sort 3 integers

firstInt = int(input("Enter the first variable: "))
secondInt = int(input("Enter the second variable: "))
thirdInt = int(input("Enter the third variable: "))

originalList = [firstInt, secondInt, thirdInt]

print(originalList)

for i in range(len(originalList)):
    if(originalList[i] != originalList[len(originalList)-1]):
        if (originalList[i] < originalList[i+1]):
            print("Comparing " + str(originalList[i]) + " and " + str(originalList[i+1]))
            temp = originalList[i]
            originalList[i] = originalList[i+1]
            originalList[i+1] = temp
            print(originalList)
    else:
        if (originalList[0] < originalList[1]):
            print("Comparing " + str(originalList[0]) + " and " + str(originalList[1]))
            temp = originalList[0]
            originalList[0] = originalList[1]
            originalList[1] = temp
            print(originalList)
            
            
            
#Question 6 in separate file
            
#Question 7


            
            

        

    
    

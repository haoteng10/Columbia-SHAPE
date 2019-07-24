# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:55:53 2019

@author: ht2531
"""
#Compare xyz with dictionary

#Dictionary
#x=y=z=0 game ended
#x=y=0 --> losing position, take z
#x=0 --> winning postion



def convertToCorrectOrder(madeList):
    #madeList = [x,y,z]
    madeList.sort()
    madeList.reverse()
    return madeList
    
def findPossibleCombination(starterList):
    #starterList = [x,y,z]
    possibleList = []
    
    #[x-a, 0, 0] [0,y-a,0] [0,0,z-a]
    for i in starterList:
        for a in range(1, i+1):
            if (starterList[0]-a >= 0):   
                possibleList.append([starterList[0]-a, starterList[1], starterList[2]])
            if (starterList[1]-a >= 0):
                possibleList.append([starterList[0], starterList[1]-a, starterList[2]])
            if (starterList[2]-a >= 0):
                possibleList.append([starterList[0], starterList[1], starterList[2]-a])
            
    for i in range(len(possibleList)):
        possibleList[i] = convertToCorrectOrder(possibleList[i])
        
    #Remove duplicated lists
    processed_set = set(map(tuple,possibleList))  #need to convert the inner lists to tuples so they are hashable
    processedList = list(map(list,processed_set))
    
    print(processedList)
    
    tempList = processedList
    
    layer=len(processedList)-1
    while(([1,0,0] not in tempList) and (layer >= 0)):
         tempList.append(findPossibleCombination(processedList[layer]))
         layer -= 1
    
        
    return processedList

def checkItem(inputList):
    # [x,y,z]
    
    if (inputList[0] == inputList[1] or inputList[0] == inputList[2] or inputList[1] == inputList[2]):
        return True
    else:
        return False
    
def theGame(userInput):
    result = []
#    returnedList = findPossibleCombination(userInput)
#    for i in returnedList:
#        result.append(findPossibleCombination(i))
#    for sublist in result:
#        for value in sublist:
#            if (value in ultimateList):
#                return value
#            else:
#                findPossibleCombination(value)
#                
    return result
    
ultimateList = []
returnedValue = findPossibleCombination([1,2,3])
#returnedValue = checkItem([3,2,2])
#returnedValue = theGame([3,2,2])
print(returnedValue)
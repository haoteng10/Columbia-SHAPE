# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:55:35 2019

@author: ht2531
"""

def findFactors(input):
    factors = [1]
    createdList = range(1,input)
    for item in createdList:
        for multiplier in range(item, input):
            if ((item * multiplier) == input):
                factors.append(item)
                factors.append(multiplier)
    return factors
        
   
def isPerfect(input):
    resultedFactors = findFactors(input)
    total = 0
    for i in resultedFactors:
        total += i
    if (total == input):
        return True
    else:
        return False
    
print(isPerfect(50))

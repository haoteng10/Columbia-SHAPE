# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:31:52 2019

@author: ht2531
"""

#Merge Sort

requiredSortingList = [6,2,5,4,7,8,8,100, 256, -5, 10000]
#
#def splitArray(inputList):
#    firstHalf = []
#    secondHalf = []
#    
#    #secondNumber = None
#    #Split the array
#    
#    if (len(inputList) == 2):
#        return inputList
#    else:
#        for item in inputList:
#            if (inputList.index(item) < int((1/2) * len(inputList) + 1)):
#                firstHalf.append(item)
#            else:
#                secondHalf.append(item)
#        return [firstHalf, secondHalf]
#
#def merge(inputOne, inputTwo):
#    if(inputOne > inputTwo):
#        return [inputTwo, inputOne]
#    else:
#        return [inputOne, inputTwo]
#    
#
#def mergeSort(inputList):
#    outputBigArray = splitArray(inputList)
#    temp = []
#    
#    print("L" + str(len(outputBigArray)))
#    while(len(outputBigArray) != int(len(inputList)/2)):
#        for individualArray in outputBigArray:   
#            temp = splitArray(individualArray)
#    
#    return temp
#
#print(mergeSort(requiredSortingList))

#MergeSort #2

def mergeSort(arr):
    if len(arr) > 1:
        #print("Splitting..." + str(arr))
        mid = int(len(arr) * (1/2))
        firstHalf = arr[:mid]
        secondHalf = arr[mid:]
        
        mergeSort(firstHalf)
        mergeSort(secondHalf)
        
        #Actual Sorting
        firstIndex = 0
        secondIndex = 0
        thirdIndex = 0
        
        #When both are not done:
        while firstIndex < len(firstHalf) and secondIndex < len(secondHalf):
            if firstHalf[firstIndex] < secondHalf[secondIndex]:
                arr[thirdIndex] = firstHalf[firstIndex]
                firstIndex += 1
            else:
                arr[thirdIndex] = secondHalf[secondIndex]
                secondIndex += 1
            thirdIndex += 1
        
        #print(firstIndex < len(firstHalf))
        
        #When one of them are done:
        while firstIndex < len(firstHalf):
            arr[thirdIndex] = firstHalf[firstIndex]
            firstIndex += 1
            thirdIndex += 1
        while secondIndex < len(secondHalf):
            arr[thirdIndex] = secondHalf[secondIndex]
            secondIndex += 1
            thirdIndex += 1
        
    #print("Merging..." + str(arr))
    return arr
       


#Heap Sort

print("===============================================================")

#finalResult = []
#
#def heapSort(inputArray):
#    
#    if(len(inputArray) > 0):
#        
#        printList = [-1,-1]
#        printList[0] = inputArray[0]
#        printList[1] = inputArray[len(inputArray) - 1]
#        print(printList)
#        
#        #Actual Sorting
#        if (inputArray[0] > inputArray[len(inputArray) - 1]):
##            temp = inputArray[0]
##            inputArray[0] = inputArray[len(inputArray) - 1]
##            inputArray[len(inputArray) - 1] = temp
#            finalResult.insert(0, inputArray[len(inputArray)-1])
#            inputArray.pop(0)
#            
#        
#        
#        
#        print("..."+ str(inputArray))
#        print(finalResult)
#
#        heapSort(inputArray)                
#        return inputArray
#
#print(heapSort(requiredSortingList))
#print("Is that heap sort?")
#            

#newList = [4,3,1,8,2,7]
#[4,3,1,8,2,7]
#[1,3,4,8,2,7]
#[]

def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1
 
def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
heapsort(alist)
print('Heap Sort......Sorted list: ', end='')
print(alist)
output = mergeSort(alist)
print("Merge Sort......Sorted list: " + str(output)) 

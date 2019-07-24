# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:29:51 2019

@author: ht2531
"""










# List l with N items
# Item's complexity
#???
#log base2 n steps (Even no.)
#log base2 n steps +1 (Other no.)

#Order n^2



#
items = int(input("Your input:"))
result = 1

if (items > 1):
    for i in range(items):
        result = result * (i+1)
        
print(result)




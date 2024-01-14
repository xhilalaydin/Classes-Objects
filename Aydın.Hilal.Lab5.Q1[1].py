# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:39:02 2023

@author: hilala-ug
"""

def pair_sum(listo):
    new=[]
    for i in range(0,len(listo),2):
        if (i+1) <len(listo):
            summ = listo[i] + listo[i+1]
            new.append(summ)
        else: 
            summ1 = listo[i]
            new.append(summ1)
    return new


ogList =[2, 8, 5, 9 , 6]
a= pair_sum(ogList)
print(f"Pair sum list: {a}")
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:25:13 2023

@author: hilala-ug
"""
"""
a. Write a function select_tuples() which takes a tuple as a parameter and
returns a new tuple containing the tuples in the input tuple.
b. Write a script that initializes a tuple and finds its tuple elements using the
select_tuples() function. Display the returned tuple.
Sample Run 1:
input tuple: (5, 'ab', (1, 4), 4.3, 'xyz', (2, 'a'))
tuples in input tuple: ((1, 4), (2, 'a'))
Sample Run 2:
input tuple: (5, 'ab', (1, 4, (3, 5)), 4.3, 'xyz', (2, 'a', [2, 7]))
tuples in input tuple: ((1, 4, (3, 5)), (2, 'a', [2, 7]))
Sample Run 3:
input tuple: (5, 'ab', [1, 4, (3, 5)], 4.3, 'xyz', (2, 'a', (2, 7)))
tuples in input tuple: ((2, 'a', (2, 7)),)
"""

def select_tuples(tup):
    new=[]
    for i in range(len(tup)):
        if type(tup[i])== tuple:
            new.append(tup[i])
    return tuple(new)


tuple1= (5, 'ab', (1, 4), 4.3, 'xyz', (2, 'a'),(2,3,4))
tuples= select_tuples(tuple1)
print(tuples)
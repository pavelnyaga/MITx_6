# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:10:00 2017

@author: Pavel
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    
    for i in aDict:
        for j in range(len(aDict[i])):
            result += 1
    
    return result

print(how_many(animals))
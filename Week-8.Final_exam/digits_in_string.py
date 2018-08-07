# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 22:10:29 2017

@author: Pavel
"""

def sum_digits(s):
    counter = 0
    sm = 0

    for i in s:
        if i.isdigit():
            counter += 1
            sm += int(i)

    if counter:
        return sm
    else:
        raise ValueError('could not find digits in s')
        

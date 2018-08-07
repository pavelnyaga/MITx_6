# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:58:19 2017

@author: Pavel
"""

#Assume s is a string of lower case characters.
#
#Write a program that counts up the number of vowels contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:
#    Number of vowels: 5

s = 'azcbobobegghakl'

#program 1
#count = 0
#
#for char in s:
#    if char in ['a', 'e', 'i', 'o', 'u']:
#        count += 1
#
#print(count)

#program 2

#count = 0
#
#for k in range(len(s)):
#    if s[k:k+3] == 'bob':
#        count += 1
#
#print(count)

# program 3

#ab = "abcdefghijklmnopqrstuvwxyz"

#s = 'abcbcd'
#s = 'zyxwvutsrqponmlkjihgfedcba'

soutmax = ""
scur = ""
countmax = 0
countcur = 0

for i in range(len(s)):
    countcur = 1
    scur = s[i]
    
    for k in range(i,len(s)-1):        
        if s[k] <= s[k+1]:
            countcur += 1
            scur = scur + s[k+1]
        else:
            break
    
    if countcur > countmax:
        countmax = countcur
        soutmax = scur

print("Longest substring in alphabetical order is: ", soutmax)
        



















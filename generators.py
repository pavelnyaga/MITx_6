# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 22:24:41 2017

@author: Pavel
"""

def genPrimes():
    primes = []
    
    i = 0
    
    while True:
        
        flag = False
        
        for p in primes:
            if (i % p) == 0:
                flag = True
                break
        
        i += 1
        
        if not flag:
            primes.append(i)        
            yield i

print(genPrimes())
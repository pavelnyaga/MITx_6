# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:48:54 2017

@author: Pavel
"""

# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def remBalanceMPR (bal0, air, mpr, k):
    rb = bal0
    
    for i in range(0,k):
        rb = rb-mpr*rb +air/12.0*(rb-mpr*rb)
    
    return rb
    
#for i in range(0,12):
#    print("Month "+ str(i+1) + " Remaining balance: " + \
#          str(round(remBalance(balance, annualInterestRate, monthlyPaymentRate, i),2)))

#print("Remaining balance: " + \
#            str(round(remBalance(balance, annualInterestRate, monthlyPaymentRate, 12),2)))


# Test Case 1:
balance = 4773
annualInterestRate = 0.2

def remBalanceFixed (bal0, air, pay):
    rb = bal0
    
    for i in range(0,12):
        rb = rb-pay + air/12.0*(rb-pay)
    
    return rb

#step = 10.0
#guess = 0.0
#
#while remBalanceFixed (balance, annualInterestRate, guess) > 0:
#    guess += step

#print ("Lowest Payment: " + str(int(guess)))

# Test Case 1:
balance = 320000
annualInterestRate = 0.2

epsilon = 0.01
low = balance/12.0
high = (balance*(1+annualInterestRate/12.0)**12)/12.0
guess = (high + low)/2.0

while abs(remBalanceFixed (balance, annualInterestRate, guess)) > epsilon:
    if remBalanceFixed (balance, annualInterestRate, guess) > 0:
        low = guess
    else:
        high = guess
    
    guess = (high + low)/2.0
print ("Lowest Payment: " + format(guess,".2f"))
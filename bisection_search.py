# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 13:42:19 2017

@author: Pavel
"""

#cube = 54
#epsilon = 0.01
#num_guesses = 0
#low = 0
#high = cube
#guess = (high + low)/2.0
#
#while (abs(guess**3-cube)) >= epsilon:
#    if guess**3 < cube:
#        low = guess
#    else:
#        high = guess
#    guess = (high + low)/2.0
#    num_guesses +=1
#print('num_guesses =', num_guesses)
#print(guess, 'is close to the root of', cube)

#epsilon = 1
num_guesses = 0
low = 0
high = 100
guess = (high + low)//2
user_input = ''

print('Please think of a number between 0 and 100!')

while True:
    print ('Is your secret number ', guess, '?', sep ='') 
    print('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. \
          Enter ''c'' to indicate I guessed correctly.', end ='')
    
    user_input = input();
    if user_input not in ['h','l','c']:
        print('Sorry, I did not understand your input.')
        continue
    else:
        if user_input == 'c':
            print('Game over. Your secret number was:', guess)
            break
        else:
            if user_input == 'h':
                high = guess
            elif user_input == 'l':
                low = guess
            
            guess = (high + low)//2
            num_guesses +=1
    
#print('num_guesses =', num_guesses)

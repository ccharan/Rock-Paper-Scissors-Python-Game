# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 00:44:27 2021

ROCK PAPER SCISSOR - GAME

@author: Charan C
"""

from random import choice


choices = ['rock', 'paper', 'scissor']
count = 3

while True:
    your_count = 0
    computer_count = 0
    
    print('*** rock paper scissor ***')
    
    for i in range(count):
        computer_choice = choice(choices)
        your_input = input('Enter your choice : ').lower()

        print("Your choice : {} <---> Computer choice : {}".format(your_input.upper(),
                                                                   computer_choice.upper()))

        if your_input in choices:
            if computer_choice == your_input:
                print('Tie')
            elif computer_choice == 'rock' and your_input == 'paper':
                print('You Win')
                your_count += 1
            elif computer_choice == 'paper' and your_input == 'scissor':
                print('You Win')
                your_count += 1
            elif computer_choice == 'scissor' and your_input =='rock':
                print('You Win')
                your_count += 1
            else:
                print('Computer Win')
                computer_count +=1
        else:
            print('ERROR!!!')

    print()
    
    if your_count == computer_count:
        print('==========')
        print('ITS TIE!!!')
        print('==========')
    elif your_count > computer_count:
        print('==========')
        print('YOU WON!!!')
        print('==========')
    else:
        print('===============')
        print('COMPUTER WON!!!')
        print('===============')

    print()

'''
In golf, pars for a hole range from 3 to 5.  Write a program using a while statement that allows the user 
to input the par and the score for each of the 18 holes.  Based on the number of shots compared to par, the program writes out the following:

"invalid score", for less than 3 under par
"albatross", for 3 under par
"eagle", for 2 under par
"birdie", for 1 under par
"bogey", for 1 over par
"double bogey", for 2 over par
"triple bogey", for 3 over par
"bad hole", for scores more than 3 over par
The input/output should look like this:

Par of hole 1: 5
Score on hole 1: 6
bogey
Par of hole 2: 4
Score on hole 2: 4
par
Par of hole 3: 3
Score on hole 3: 5
double bogey
Par of hole 4: 4
Score on hole 4: 3
birdie

etc.
'''

import sys
from random import randint
import math
choice1=input("would you like to play a game of rock,paper and scissors: ")
while choice1=="yes":
    choice2=input("please choose rock,paper or scissor: ")
    computer=randint(1,3)
    score=0
    score2=0
    if choice2 in ("rock","paper","scissor"):
        if computer==1:
            print("You have chosen "+ choice2 + " and the computer has chosen rock ")
            if choice2=="rock":
                print("It'/s a draw ")
            elif choice2=="paper":
                print("You win! ")
                score += 1
            elif choice2=="scissor":
                print("You lose :( ")
                score2 += 1 
            else:
                sys.exit()
        elif computer==2:
            print("You have chosen " + choice2 + " and the computer has chosen paper ")
            if choice2=="rock":
                print("You lost :( ")
            elif choice2=="paper":
                print("It'/s a draw")
            elif choice2=="scissor":
                print("You won! ")
            else:
                sys.exit()
        elif computer==3:
            print("You have chosen " + choice2 + " and the computer has chosen scissor ")
            if choice2=="rock":
                print("You won! ")
            elif choice2=="paper":
                print("you lost :( ")
            elif choice2=="scissor":
                print("It'/s a draw ")
            else:
                sys.exit()
        choice3=input("Would you like to play again? Type yes or no: ")
        if choice3=="no":
            print (score)
            print (score2)
            sys.exit()
    else:
        sys.exit()
else:
    print("GoodBye")
    sys.exit()
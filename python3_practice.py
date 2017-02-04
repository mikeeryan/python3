# -*- coding: utf-8 -*-
"""
Various Python3 codes for practice and fun
by Michael Eryan
"""

#Print all elements less than the user input
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l = input("Enter the upper (exclusive) boundary number")

#pretty solution, key: list is an iterable
out = []
for i in a:
    if  i < int(l):
        out.append(i)
print(out)

#a better way - use a list comprehension
out2 = [element for element in a if element < int(l)]
print (out2)

#Calculate age in years - For loop vs list comprehension
#Get current year first
from datetime import date
cur_year = date.today().year
print (cur_year)
#List of birth years
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []
for year in years_of_birth:
    ages.append(cur_year - year)
print (ages)

#Alternatively - use a list comprehension
ages = []
ages = [cur_year - year for year in years_of_birth]
print (ages)

#Another cool way to use list comprehensions - permutate all possible pairs where x does not equal y
pairs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print (pairs)


#Shoppting list program - prompt user to enter one item at a time
# DONE quits the program and ouputs the result, SHOW prints the current list, HELP shows what the special commands DONE

slist = []
def shop_fn():
	prompt = input("Enter your item or command (not case sensitive): ")
	if prompt.upper() == "HELP":
		print ("DONE quits the program and outputs the full list")
		print ("SHOW prints the current list")
		print ("HELP print what the special functions do")
		shop_fn()
	elif prompt.upper() == "SHOW":
		print (slist)
		print ("The current list contains",len(slist),"items.")
		shop_fn()
	elif prompt.upper() == "DONE":
		print (slist)
		print("The final list contains", len(slist), "items.")
	else:
        slist.append(prompt)
		shop_fn()
shop_fn()


# Rock Paper Scissor game
# Rock beats scissors Scissors beats paper Paper beats rock
# Mine will be a simple game, just to compare values that were entered

def rps():
    output = {}
    player1 = input("Player 1, enter your choice (not case sensitive):")
    output['Player 1'] = player1
    player2 = input("Player 2, enter your choice:")
    output['Player 2'] = player2
    if player1.upper() == player2.upper():
        output['Result']="Draw"
    if ( player1.upper() == 'ROCK' and player2.upper() == 'SCISSORS' ) or \
    ( player1.upper() == 'SCISSORS' and player2.upper() == 'PAPER' ) or \
    ( player1.upper() == 'PAPER' and player2.upper()=='ROCK' ):
        output['Result'] ="Player 1 Wins!"
    else:
        output['Result'] ="Player 2 Wins!"
    print (output)
    playagain = input("Play again? Yes/No")
    if playagain.upper() == 'YES':
        rps()
    else:
        print("Game Over!")
rps()


#Cows and bulls game
#every digit guessed in the right place is a cow, in the wrong place - bull
#AI's random number is a
import random
a = str(random.randint(1000, 9999))
print (a)

def guess():
    g = input("Enter your 4 digit guess, within [1000,9999]")
    cows = 0
    bulls = 0
    for i in range(4):
        if a[i] == g[i]:
            cows = cows + 1
        else:
            if a[i] in g:
                bulls = bulls + 1
    print ("Cows:", cows," and ", "Bulls:", bulls)
    if cows == 4:
        print ("You guessed correctly!")
        print ("The number is:", a)
        print ("Game Over!")
    elif g=="0000":
        print ("Game Over!")
    else:
        guess()
guess()


#Human guessing AI's number
number = random.randint(1, 9)
print (number)

#function starts below
count = 0
def humanguess(n):
    global count
    g = input("Guess between 1 and 9")
    try:
        gint = int(g)
        count += 1
        if gint < n:
            print ("Too Low!")
            humanguess(number)
        elif gint > n:
            print ("Too High!")
            humanguess(number)
        else:
            print("You got it!", g, "is the correct number!")
            print("It only took you", count, "tries!")
    except ValueError:
        if g.upper() in ['EXIT','QUIT']:
            print ("You gave up after", count, "guesses!")
        else:
            print ("You did not enter an integer or entered Exit/Quit.")
humanguess(number)


#Reversed game - AI guessing a human number, a simple binary search

#stats for the median
import statistics as stats

lower = input("Input the lower boundary of the range")
upper = input("Input the upper boundary of the range")
hnumber = input("Input your integer within the range")

#function starts below
count = 1
def aiguess(g):
    global count,lower, upper
    try:
        gint = int(g)
        lint = int(lower)
        uint = int(upper)
        li = [i for i in range(lint, uint + 1)]
        an = round(stats.median(li))
        if gint < an:
            print ("Guess #", count, "AI guessed: ",an, "which is too High!")
            upper = an
            count+=1
            aiguess(g)
        elif gint > an:
            print ("Guess #", count, "AI guessed: ",an, "which is too Low!")
            lower = an
            count+=1
            aiguess(g)
        else:
            print("AI got it!", an, " == ", g, "is the correct number!")
            print("It only took AI", count, "tries!")
    except ValueError:
            print ("You did not enter integers!")
aiguess(hnumber)

#1-100, 99 is furthest - still, only 7 tries
#1-1,000, 999 - only 10 tries
#because of rounding - closest to the upper boundary takes 1 more guess than closest to lower boundary
#pick 70 to see up and down search


#The End.
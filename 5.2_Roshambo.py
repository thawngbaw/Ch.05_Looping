'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random

bot_1 = 0
user_win = 0
game_quit = "n"
while game_quit == "n":
    c = (random.randint(1,3))

    print("1 = rock \n2 = paper \n3 = scissor")

    user_1 = int(input("enter a number from 1 - 3: "))

    if c == 1:
        print("Bot = rock")
    elif c == 2:
        print("Bot = paper")
    elif c == 3:
            print("Bot = scissor")

    if user_1 == 2 and c == 1:
        print("You win")
        user_win += 1
    elif user_1 == 1 and c == 2:
        print("You lose")
        bot_1 += 1
    elif user_1 == 3 and c == 1:
        print("You lose")
        bot_1 += 1
    elif user_1 == 3 and c == 2:
        print("You win")
        user_win += 1
    elif user_1 == 1 and c == 3:
        print("You lose")
        bot_1 += 1
    elif user_1 == 2 and c == 3:
        print("You lose")
        bot_1 += 1
    elif c == user_1:
        print("tied")

    game_quit = input("Do you want to quit (y,n)? ")
    if game_quit == "n":
        print()
        continue
    elif game_quit != "n":
        print()
        print("WINs =", user_win)
        print("Loses =", bot_1)
        break


print()
print()











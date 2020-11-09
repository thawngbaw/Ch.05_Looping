'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

import random
done = False
num_light_year = 0  # NUmber of mile
tired_level = 0
damage_level = 0
distance_bandit_travel = -20
a = 5            # amount of fuel
e = "status check"
b = "moderate speed"
c = "full speed"
d = "stop for supply"
print("You are 200 light years away from your home planet, because of some accident and you")
print(" are being chase by space bandit")
print()
print("Try to get back to your home planet safely, without dying!!!")
print()
print("Here are your choice")
print()
while not done:

    print(" A. take a rest")
    print(" B.Ahead normal speed")
    print(" C.Ahead full speed")
    print(" D.Stop to collect supply from nearby planet")
    print(" E.status check")
    user_player = input("enter your choice = ")  # ask user for their choice

    print()
    print()
    if user_player.lower() == "a":
        a -= 1
        tired_level -= tired_level
    elif a == 0:
        print("Your fuel is low")
    elif user_player.lower() == "b":
        num_light_year += random.randint(5, 12)
        print("-Number of light years travel = ", num_light_year)
        tired_level += 1
        damage_level += 1
        distance_bandit_travel += random.randint(7, 14)

    elif user_player.lower() == "c":
        num_light_year += random.randint(10, 20)
        print("-Number of light years travel", num_light_year)
        tired_level += 1
        damage_level += random.randint(1, 3)
        distance_bandit_travel += random.randint(1, 14)
    elif user_player.lower() == "d":
        damage_level -= damage_level
        print("Your ship is repaired")
        distance_bandit_travel += random.randint(7, 14)
    elif user_player.lower() == "e":
        print("-Number of light years travel", num_light_year)
        print("-Amount of fuel left", a)
        print("-Distance of bandit", distance_bandit_travel)
        user_game_quit = input("Do you want to Give UP (Q, N) ")
        quit_game = "Q"
        if user_game_quit.upper() == "Q":
            print("Number of light years travel =", num_light_year)
            print("Amount of fuel left =", a)
            print("Distance of bandit =", distance_bandit_travel)
            done = True

    if not done and tired_level == 4:
            print("you are tired")
    elif tired_level >= 6:
        print("You die because you over work your body")
        print("-Number of light years travel =", num_light_year)
        print("-Amount of fuel left =", a)
        print("-Distance of bandit =", distance_bandit_travel)
        done = True

    if not done and damage_level == 5:
            print("your ship is damage")
    elif damage_level >= 8:
        print("Your ship has been eradicate")
        print("You Lose")
        print("-Number of light years travel =", num_light_year)
        print("-Amount of fuel left =", a)
        print("-Distance of bandit =", distance_bandit_travel)
        done = True
    bandit_catching = distance_bandit_travel - num_light_year
    if bandit_catching == 15:
        print("the bandit are catching up")
    elif distance_bandit_travel == num_light_year:
        print("The bandit have caught up")
        print("-Number of light years travel =", num_light_year)
        print("-Amount of fuel left =", a)
        print("-Distance of bandit =", distance_bandit_travel)
        done = True

    if num_light_year == 200:
        print("You Win")
        print("-Number of light years travel =", num_light_year)
        print("-Amount of fuel left =", a)
        print("-Distance of bandit =", distance_bandit_travel)
        done = True

    ocean = random.randint(1, 20)
    if ocean == 4:
        print("You found an abandoned space ship")
        tired_level -= tired_level
        a -= a
        damage_level -= damage_level
        print("Your ship has been refuel")
        print("Your ship damage has been repaired")

print()
print()



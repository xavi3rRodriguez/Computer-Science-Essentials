# single player guessing game 
# alows player to play against an ai to guess a number

#imports
import random

#variables
player_guess = -1
random_number = -1
Player_lives = 10
print("Welcome to the Single Player Guessing Game")
print("guess a number between 1-1000")

random_number = random.randint(1,1000)
while Player_lives > 0:
    try:
        player_guess = int(input("->"))
        Player_lives -= 1
        print("lives remaining", Player_lives)
        if player_guess == random_number:
            print("yipeeeeeeeeeeee you did it")
        elif player_guess > random_number:
            print("Lower")
        elif player_guess < random_number:
            print("Higher")
        elif Player_lives > 0:
            print("bad get better")
        else:
            print("<ERROR>")
    except:
        print("no")

print("thanks for playing")
print("the supper secret number was", random_number)
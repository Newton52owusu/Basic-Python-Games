# This is a simple casino game
# A particular number is infused into the algorithm of a program
# Then there is a raised amount of money  as a ransom
# Any user who gets the luck to guess that number within three
# trials wins the ransom
# Every user is expected to place an amount of $25 dollars to allow
# the game work. The winner gets $150
import pygame
pygame.font.init()


print("Hello there! Welcome to my Casino")
print("To continue playing, insert $25 dollars by\n"
      "typing 25 or 0 to quit.")
lucky_number = 8
player_input = int(input("Type here: "))
guesses = 0
guess_limit = 3

if player_input == 25:
    print("Welcome to the GAME OF CHANCES!")
elif player_input == 0:
    print("See you again next time Champ!")
    quit()
else:
    print("Invalid input")
    quit()


while guesses < guess_limit:
    user_guess = int(input("Try your luck: "))
    guesses += 1
    if user_guess == lucky_number:
        print("You won $150")
        break
else:
    print("Sorry! You lost")

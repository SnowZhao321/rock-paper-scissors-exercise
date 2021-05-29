
# game.py
import random

import os 

import dotenv

dotenv.load_dotenv()


PLAYER_NAME = os.getenv("PLAYER_NAME")
#print(PLAYER_NAME)

print("--------------------------")
print("Welcome " + PLAYER_NAME + " to my Rock-Paper-Scissors game")
print("--------------------------")

#print(10)

#print(10, 99, "My message", "another message")

user_choice = input("Please choose either 'rock', 'paper', 'scissors': ")

#print(user_choice)
print("USER_CHOICE: ", user_choice)

# validate the input such that only if it is one of the expected values
# ... will we continue with the rest of the program
# ... otherwise we'll stop the progam before it tries to do anything else
# ... and we'll ask the user to run the program again


#if user_choice = "rock" or "paer" or "scissors": # THIS LINE IS PSEUDOCODE
# if user_choice == "rock":
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()


valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE:", computer_choice)

# determine who won!
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if (computer_choice == "paper"):
        print("oh, Computer wins! It's ok.", computer_choice, "beats", user_choice)
    elif (computer_choice == "scissors"):
        print("You win!", user_choice, "beats", computer_choice)
elif user_choice == "paper":
    if (computer_choice == "scissors"):
        print("oh, Computer wins! It's ok.", computer_choice, "beats", user_choice)
    elif (computer_choice == "rock"):
        print("You win!", user_choice, "beats", computer_choice)
elif user_choice == "scissors":
    if (computer_choice == "rock"):
        print("oh, Computer wins! It's ok.", computer_choice, "beats", user_choice)
    elif (computer_choice == "paper"):
        print("You win!", user_choice, "beats", computer_choice)
else:
    print("Oops! There was an error. Please try again.")

#configure player name via environment variables 

print("Thanks for playing. THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")
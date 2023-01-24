import random
import colorama


rock = "Rock"
paper = "Paper"
scissors = "Scissors"

# Game move logic

player_move = input("Choose [r]ock, [p]aper, [s]cissors:")

if player_move == "r" or player_move == "rock":
    player_move = rock
elif player_move == "p" or player_move == "paper":
    player_move = paper
elif player_move == "s" or player_move == "scissors":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Please try again!")

computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer_choice = rock
elif computer_choice == 2:
    computer_choice = paper
else:
    computer_choice = scissors

print(colorama.Fore.BLUE + f"Computer chose {computer_choice}.")

# Comparing moves and deciding winner

if (player_move == rock and computer_choice == scissors) or (player_move == paper and computer_choice == rock) \
        or (player_move == scissors and computer_choice == paper):
    print(colorama.Fore.GREEN + "You win!")
elif (player_move == rock and computer_choice == rock) or (player_move == paper and computer_choice == paper) \
        or (player_move == scissors and computer_choice == scissors):
    print(colorama.Fore.YELLOW + "Draw!")
else:
    print(colorama.Fore.RED + "You lose!")

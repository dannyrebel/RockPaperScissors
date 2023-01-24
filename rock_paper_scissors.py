import random
import colorama
import pyfiglet

player_score = 0
computer_score = 0

while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    # Game move logic

    player_move = input(colorama.Fore.LIGHTWHITE_EX + "Choose [r]ock, [p]aper, [s]cissors: ")

    if player_move == "r" or player_move == "rock":
        player_move = rock
    elif player_move == "p" or player_move == "paper":
        player_move = paper
    elif player_move == "s" or player_move == "scissors":
        player_move = scissors
    else:
        print("Invalid input. Please try again!")
        continue

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
        player_score += 1
    elif (player_move == rock and computer_choice == rock) or (player_move == paper and computer_choice == paper) \
            or (player_move == scissors and computer_choice == scissors):
        print(colorama.Fore.LIGHTYELLOW_EX + "Draw!")
    else:
        print(colorama.Fore.RED + "You lose!")
        computer_score += 1

    print(f"Player [{player_score}] | Computer [{computer_score}]")

    # Restarting the game

    while True:
        restart = str(input(colorama.Fore.LIGHTWHITE_EX + "Play again?: (y / n): "))
        if restart == "y" or restart == "Y":
            break
        elif restart == "n" or restart == "N":
            print(pyfiglet.figlet_format('Goodbye!', font='starwars'))
            raise SystemExit
        else:
            print(colorama.Fore.RED + "Invalid option, please confirm your choice.")
            continue

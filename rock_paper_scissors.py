import random
import colorama

player_score = 0
computer_score = 0

while True:
    rock = ["Rock", "r", "rock", 1]
    paper = ["Paper", "p", "paper", 2]
    scissors = ["Scissors", "s", "scissors", 3]

    # Game move logic

    player_move = input(colorama.Fore.LIGHTWHITE_EX + "Choose [r]ock, [p]aper, [s]cissors: ")

    if player_move in rock:
        player_move = rock[0]
    elif player_move in paper:
        player_move = paper[0]
    elif player_move in scissors:
        player_move = scissors[0]
    else:
        print("Invalid input. Please try again!")
        continue

    computer_choice = random.randint(1, 3)

    if computer_choice in rock:
        computer_choice = rock[0]
    elif computer_choice in paper:
        computer_choice = paper[0]
    else:
        computer_choice = scissors[0]

    print(colorama.Fore.BLUE + f"Computer chose {computer_choice}.")

    # Comparing moves and deciding winner

    if player_move == computer_choice:
        print(colorama.Fore.LIGHTYELLOW_EX + "Draw!")
    elif (player_move == rock[0] and computer_choice == scissors[0]) or (player_move == paper[0] and computer_choice == rock[0]) \
            or (player_move == scissors[0] and computer_choice == paper[0]):
        print(colorama.Fore.GREEN + "You win!")
        player_score += 1
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
            print("Goodbye!")
            raise SystemExit
        else:
            print(colorama.Fore.RED + "Invalid option, please confirm your choice.")
            continue
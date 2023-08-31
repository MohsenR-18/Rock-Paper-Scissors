import random

def init():
    while True:
        choices = ['rock', 'paper', 'scissors']

        computer = random.choice(choices)

        player = None
        while player not in choices:
            player = input("rock, paper, scissors?: ")

        check_the_winner(computer, player)

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Bye!")
# *****************************************************************
def check_the_winner(computer, player):
    print()
    if computer == player:
        print_result(computer, player, "tie")
    elif player == "paper":
        if computer == "scissors":
            print_result(computer, player, "lose")
        if computer == "rock":
            print_result(computer, player, "win")
    elif player == "rock":
        if computer == "scissors":
            print_result(computer, player, "win")
        if computer == "paper":
            print_result(computer, player, "lose")
    elif player == "scissors":
        if computer == "paper":
            print_result(computer, player, "win")
        if computer == "rock":
            print_result(computer, player, "lose")
    print()
# *****************************************************************
def print_result(computer, player, status):
    print("computer: " + computer)
    print("player: " + player)

    if status == "tie":
        print("Tie!")
    elif status == "win":
        print("You Win!")
    elif status == "lose":
        print("You lose!")
# *****************************************************************

init()

import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose rock, paper, or scissors.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("Rock, Paper, Scissors Game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

 
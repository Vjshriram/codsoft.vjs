import random
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == "rock" and computer_choice == "scissors"):
        return "you win buddy",1
    elif (user_choice == "paper" and computer_choice == "rock"):
        return "you win buddy",1
    elif (user_choice == "scissors" and computer_choice == "paper"):
        return "you win buddy",1
    else:
        return "you lost buddy!", -1

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Your choice:",user_choice)
        print("Computer's choice:",computer_choice)
        result, score = determine_winner(user_choice, computer_choice)
        print(result)
        user_score += score
        computer_score -= score
        print("Score - You:",user_score,"Computer:",computer_score)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "no":
            print("the final result:","\nYour score:",user_score,"\ncomputer score:",computer_score)
            break

play_game()

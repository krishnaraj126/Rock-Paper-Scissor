import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player} and computer chose {computer}")
    
    if player == computer:
        return "It's a Tie!"
    
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! Player wins."
        else:
            return "Paper covers rock! You Lose."
    
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! Player wins."
        else:
            return "Scissors cuts paper! You Lose."
    
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! Player wins."
        else:
            return "Rock smashes scissors! You Lose."

    else:
        return "Invalid input! Please choose rock, paper, or scissors."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

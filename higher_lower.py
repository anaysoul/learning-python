from higher_lower_art import logo, vs 
import random, os
from game_data import data 

def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_follower = account["follower_count"]
    account_country = account["country"]
    return f"{account_name} {account_description} {account_country}"

## use if statement to check if user is correct
def check_answer(guess, a_followers, b_followers):
    """take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


#Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# make the game repeat until lose a round
while game_should_continue:
    # generate a random acct from the game Data
    account_a = account_b
    account_b = random.choice(data)
    
    #making account at position b become the next account at position a
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #ask user for a guess 
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #check if user is correct
    ## get follower count for each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #clear the screen between rounds
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    # give user feedback on their guesses
    #score keeping 
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else: 
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False

  
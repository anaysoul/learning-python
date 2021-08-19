# ###### Scope #################################################################
# enemies = 1 

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# # Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# # print(potion_strength)

# # global scope 
# player_health = 100

# def game():
#     def drink_potion():
#         potion_strength = 21
#         print(player_health)
#     drink_potion()

# print(player_health)

# # if 3 > 2:
# #     a_variable = 10

# # There is no block scope for python
# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

# enemies = 1 
# # avoid modifiying global scope
# def increase_enemies():
#     print(f"Enemies inside function: {enemies}")
#     return enemies + 1

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# #global constants define and not change again

# PI = 3.14159
# URL = "http://www.python.org"

# Number Guessing Game 
from random import randint 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# make function to set difficulty
def set_difficulty():
    level = (input ("Choose a difficulty. Type 'easy' or 'hard': "))
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. ")

    # choose a random number between 1 and 100
    answer = randint(1, 100)
    print(f"psst, the number is {answer}")
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")
        # let the user guess a number 
        guess = int(input("Make a guess: "))
        # check user guess against answer
        turns = check_answer(guess, answer, turns)

        if turns == 0 and guess != answer:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer: 
            print("Guess again.")
# repeat 
game()




# # day-1-printing-start
# print("Hello world!");
# print('Day 1 - Python Print Functions');
# print("The function is declared like this:");
# print("print('what to print')");

# print("Hello " + "Angela");

# # input function
# print("Hello " + input("What is your name? "));

# # challenge input function 
# name = input("What is your name? ");
# print(len(name));

# Variables
# name = input("What is your name? ");
# print(name);

# name = "Jack";
# print(name);

# Variable exercise
# 🚨 Don't change the code below 👇
# a = input("a: ")
# b = input("b: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# inputA = a;
# inputB = b;
# a = inputB;
# b = inputA;



# #Write your code above this line 👆
# ####################################

# # 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)

# # Project 1: Band Name Generator
# print("Greetings to the Band Name Generator bot!");
# city = input("What city did you grow up in?\n");
# pet = input("What is the name of your pet?\n")
# print("Your rockstar band name is " + city + " " + pet + "!");

# Project 2: Tip Calculator
# print("Welcome to the tip calculator bot!");
# total = float(input("What was the total bill?\n"));
# split = int(input("How many people to split the bill?\n"));
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"));
# # print(type(split));
# # print(type(tip));
# # print(type(total));
# tip_amount = total* (tip/100);
# tip_per_person = (total + tip_amount) / split;
# tip_per_person = "{:.2f}".format(tip_per_person);
# print(f"Each person should pay: ${tip_per_person}");

# Data Types Exercise
# two_digit_number = input("Type a two digit number: \n");
# a = int(two_digit_number[0]);
# b = int(two_digit_number[1]);
# ab = str(a + b);
# print(str(a) + " + " + str(b) + " = " + ab );

# BMI Calculator Exercise
# height = float(input("enter your height in m: "));
# weight = float(input("enter your weight in kg: "));

# bmi = int(weight / (height ** 2));
# print("Your BMI is " + str(bmi));

# # f-string
# score = 0;
# height = 1.8
# isWinning = True
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}");

# Life in Weeks
# age = int(input("What is your current age? \n"));
# remaining_years = 90 - age;
# days = (remaining_years * 365);
# weeks = (remaining_years * 52);
# months = (remaining_years * 12);
# print(f"You have {days} days, {weeks} weeks and {months} months left!");

# Control flow of if/else statements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"));

# if height > 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, shorty!")

# # Exercise 3.1: Odd or Even
# number = int(input("Which number do you want to check? \n"));
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number")

# # Nested if/else statements and elif
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"));

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Please pay $5!")
#     elif age <= 18:
#         print("Please pay $7!")
#     else:
#         print ("Pay $12!");
# else:
#     print("Sorry, shorty!")

# BMI 2.0 
# height = float(input("What is your height in m? "))
# weight = float(input("What is your weight in kg? "))
# BMI = round(weight / (height ** 2.0))

# if BMI <= 18.5:
#     print(f"Your BMI is {BMI}; you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}; you hava a normal weight");
# elif BMI < 30: 
#     print(f"Your BMI is {BMI}; you are overweight!")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}; you are obese!!")
# else:
#     print(f"Your BMI is {BMI} and you are clinically obese!!!");

# Day 3.3 Leap year
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     print("Leap Year!")    
# elif year % 100 == 0:
#     print("Not leap year")
# elif year % 400 == 0:
#     print("Leap year!") 
# else:
#     print("Not Leap Year!")

# instructor solution
# if year % 4 == 0:  
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year!") 
#     else:
#         print("Leap year!")
# else:
#     print("Not Leap Year!")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"));
# bill = 0

# if height > 120:
#     print("You can ride the rollercoaster!\n")
#     age = int(input("What is your age?\n"))
#     if age < 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     else:
#         bill = 12

#     wants_photo = input("Do you want a photo taken? Y or N \n")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your total bill due is ${bill}.")
# else:
#     print("Sorry, shorty!")

# Exercise 3.4 Pizza Order
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L \n")
# add_pepperoni = input("do you want pepperoni? Y or N \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")

# bill = 0
# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# elif size == "L":
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# print(f"Your final bill is: ${bill}")

# instructor solution 
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2 
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}")

# Logical operators 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"));
# bill = 0

# if height > 120:
#     print("You can ride the rollercoaster!\n")
#     age = int(input("What is your age?\n"))
#     if age < 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok! Enjoy a free ride on us! :)")
#     else:
#         bill = 12

#     wants_photo = input("Do you want a photo taken? Y or N \n")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your total bill due is ${bill}.")
# else:
#     print("Sorry, shorty!")

# # 3.5 Love Calculator
# print("Welcome to the Love Calculator!\n")
# name1 = input("What is your name?\n")
# name2 = input("What is their name?\n")

# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# t = lower_case_string.count("t")
# r = lower_case_string.count("r") 
# u = lower_case_string.count("u")
# e = lower_case_string.count("e") 
# l = lower_case_string.count("l")
# o = lower_case_string.count("o") 
# v = lower_case_string.count("v") 

# true = t + r + u + e
# love = l + o + v + e

# love_score = str(true) + str(love)
# total_love_score = int(love_score)

# if total_love_score < 10 or total_love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif total_love_score >= 40 and total_love_score <= 50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")

# # Day 3 Project: Treasure Island
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# direction = input("left or right?")
# if (direction == "left"):
#     motion = input("swim or wait?")
#     if (motion == "wait"):
#         door = input("Which door?")
#     else:
#         print("GAME over!")
#     if (door == "yellow"):
#         print("You Win!")
#     else:
#         print("Game Over!")
# else:
#     print("GAME OVER!")

# import random

# randomInteger = random.randint(0, 1)
# if (randomInteger == 0):
#     print("Tails")
# else:
#     print("Heads")

# Lists
# states_of_america = ["Delaware", "Pennsylvania", "Maryland"]

# Banker Roulette - who will pay the bill?
# import random 

# names_string = input("Give me everyones names, seperated by a comma. ")
# names = names_string.split(",")

# dice = random.randint(0, len(names) - 1 );
# print(f"{names[dice]} will pay the bill today!")
# print(f"{random.choice(names)} will pay the bill");

# Treasure Map exercise
# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "x"





# Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# Rock-paper-scissors project
# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
# computer_choice = random.randint(0,2)
# if user_choice == 0:
#     print(rock)
# elif user_choice == 1:
#     print(paper)
# elif user_choice == 2:
#     print(scissors)
# else:
#     print("Please make sure you choose 0 for Rock, 1 for Paper or 2 for Scissors. ")
# print("Computer's choice: ")
# if computer_choice == 0:
#     print(rock)
# elif computer_choice == 1:
#     print(paper)
# elif computer_choice == 2:
#     print(scissors)
# else:
#     print("Please make sure you choose 0 for Rock, 1 for Paper or 2 for Scissors. ")

# if (user_choice == 0 and computer_choice == 0):
#     print("Draw!")
# if (user_choice == 0 and computer_choice == 1):
#     print("computer wins")
# if (user_choice == 0 and computer_choice == 2):
#     print("user wins")
# if (user_choice == 1 and computer_choice == 0):
#     print("user wins")
# if (user_choice == 1 and computer_choice == 1):
#     print("Draw!")
# if (user_choice == 1 and computer_choice == 2):
#     print("computer wins")
# if (user_choice == 2 and computer_choice == 0):
#     print("computer wins")
# if (user_choice == 2 and computer_choice == 1):
#     print("user wins")
# if (user_choice == 2 and computer_choice == 2):
#     print("Draw!")

#instructor solution
# game_images = [rock, paper, scissors]
# print("User Choice: ")
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!") 
# else:
#     print(game_images[user_choice])

#     print(f"Computer Choice: {game_images[computer_choice]}")

#     if (user_choice == 0 and computer_choice == 2):
#         print("You Win!")
#     elif computer_choice == 0 and user_choice == 2:
#         print("You Lose!")
#     elif computer_choice > user_choice:
#         print("You Lose!")
#     elif user_choice > computer_choice:
#         print("You Win!")
#     elif computer_choice == user_choice:
#         print("Draw!")



# Exercise 5.1 Average Height
# student_heights = input("Inpur a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_heights = 0
# counter = 0
# for height in student_heights:
#     total_heights += height
#     counter += 1
# print(total_heights)
# avg_height = round(total_heights / counter)
# print(avg_height)

# 5.2 highest score
# student_scores = [78, 65, 89, 96, 55, 91, 64, 89]
# high_score = 0 
# for score in student_scores:
#     if (score > high_score):
#         high_score = score
# print(f"The highest score in the class is: {high_score}")

#  for loop with range
# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# 5.3 Adding evens
# total = 0 
# for number in range(1, 101):
#     if (number % 2 == 0):
#         total += number
# print(f"The sum of all even numbers is {total}")

# 5.4 Fizz Buzz 
# for num in range(1, 101):
#     if (num % 3 == 0 and num % 5 == 0):
#         print("FizzBuzz")
#     elif (num % 3 == 0):
#         print("Fizz")
#     elif (num % 5 == 0):
#         print("Buzz")
#     else:
#         print(num)

# PyPassword Generator
#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# # password = ""
# # for num in range(1, nr_letters + 1):
# #     # 1 - 4
# #     random_num = random.choice(letters)
# #     password += random_num
# # # print(password)

# # for num in range(1, nr_symbols + 1):
# #     # 1 - 2 
# #     random_num = random.choice(symbols)
# #     password += random_num 
# # # print(password)

# # for num in range(1, nr_numbers + 1):
# #     # 1 - 2 
# #     random_num = random.choice(numbers)
# #     password += random_num
# # print(password)

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# # random_pw = ""
# # for num in range(0, len(password)):
# #     random_pw += random.shuffle(password)
# # print(random_pw)
# # random_pw = random.shuffle(password)
# # print(random_pw)

# #instructor solution hard level 
# password_list = []
# for num in range(1, nr_letters + 1):
#     # 1 - 4
#     password_list.append(random.choice(letters))
# # print(password)

# for num in range(1, nr_symbols + 1):
#     # 1 - 2 
#     password_list += random.choice(symbols)
    
# # print(password)

# for num in range(1, nr_numbers + 1):
#     # 1 - 2 
#     password_list += random.choice(numbers)
    
# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# random_pw = ""
# for char in password_list:
#     random_pw += char 
# print(random_pw)

# print("Hello")
# num_char = len("Hello")
# print(num_char)

# def my_function():
#     print("Hello")
#     print("Bye")


# import random
# from hangman_words import word_list
# from hangman_art import stages, logo 

# # my_function()
# chosen_word = random.choice(word_list)
# end_of_game = False
# word_length = len(chosen_word)
# lives = 6

# # print hangman logo
# print(logo)

# #Testing code
# print(f"Psst, the solution is {chosen_word}") 

# # Create blanks
# display = []
# for char in range(word_length):
#     display.append("_")
# print(display)


# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     # notify user of repeating guesses
#     if guess in display:
#         print(f"You've already guessed {guess}")

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = guess
#     if guess not in chosen_word:
#         lives -= 1
#         print(f"Wrong guess: {guess}! Lives: {lives}")
#         if lives == 0:
#             end_of_game = True
#             print("You lose!")
#     print(display)
#     if "_" not in display:
#         end_of_game = True
#         print("You win!")
#     # Display hangman
#     print(stages[lives])

# def greeting(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greeting(name="Jack Bauer", location="nowhere")

# Calculate area
# import math

# def paint_calc(height, width, cover):
#     area = (height * width) 
#     num_of_cans = math.ceil(area / cover)
#     print(f"You'll need {num_of_cans} cans of paint to cover {cover} sq meters of area")

# coverage = 5
# paint_calc(3, 9, coverage)

#  prime number checker

# def prime_checker(number):
#     prime = True
#     for num in range(2, number - 1):
#         if number % num == 0:    
#             prime = False
#     if(prime == True):
#         print("It is a prime number")
#     else:
#         print("It is not a prime number")

# n = int(input("Check this number: "))
# prime_checker(number = n)
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text, shift, direction):
    new_text = ""
    shift %= 26
    for char in text:
        if char in alphabet: 
            position = alphabet.index(char)
            if direction == "encode":
                new_position = position + shift
            elif direction == "decode":
                new_position = position - shift
            new_letter = alphabet[new_position]
            new_text += new_letter
        else:
            new_text += char
    print(f"The {direction}d message is {new_text}")

should_contine = True
while should_contine:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    result = input("Type 'y' if you want to go again. Otherwise type 'n'. " )
    if result == "y":
        sould_contine = True
    else:
        should_contine = False
        print("Goodbye!")



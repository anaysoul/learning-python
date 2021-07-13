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
print("Welcome to the tip calculator bot!");
total = float(input("What was the total bill?\n"));
split = int(input("How many people to split the bill?\n"));
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"));
# print(type(split));
# print(type(tip));
# print(type(total));
tip_amount = total* (tip/100);
tip_per_person = (total + tip_amount) / split;
tip_per_person = "{:.2f}".format(tip_per_person);
print(f"Each person should pay: ${tip_per_person}");

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

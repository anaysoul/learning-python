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
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0
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
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2 
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
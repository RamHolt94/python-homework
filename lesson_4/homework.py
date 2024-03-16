# Homework Lesson 4 - Conditionals

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 1: Temperature Classification
# You're developing a weather application. Write a program that takes 
# a temperature in Fahrenheit as input. If the temperature is above 
# 85°F, print "Hot day ahead!".
temperature = int(input("Enter the temperature in Fahrenheit: "))

temperature = int(input("Enter the temperature in Fahrenheit: "))
if temperature > 85:
    print("Hot day ahead!")
else:
    print("Cold day ahead!")

# ---------------------------------------------------------------------
# Exercise 2: Grade Classifier
# As a teacher, you want to automate grading. Write a program that
# takes a student's score as input and prints "Pass" if the score is
# 50 or above, otherwise print "Fail".
# Do not forget that the input() function returns a string value and
# you need to convert it so you can use the value as a number.

students_score = input("Enter score: ")
if students_score >= 50:
    print("Pass")
else:
    print("Fail")

# ---------------------------------------------------------------------
# Exercise 3: Scholarship Eligibility
# Your university offers scholarships based on academic performance.
# Write a program that takes a student's GPA as input. If the GPA
# is greater than or equal to 3.5, print
# "Congratulations, you're eligible for a scholarship!". If it's
# between 3.0 and 3.49, print "You're on the waiting list."
# Otherwise, print "Keep up the good work."
# Do not forget that the input() function returns a string value and
# you need to convert it so you can use the value as a number.
# The function int() converts the number to an integer, and the function
# float() converts the number to a float.


gpa = float(input("Enter your GPA: "))
if int(gpa) >= 3.5:
    print("Congratulations, you're eligible for a scholarship!")
elif int(gpa) == 3.49 and > 3.0:
    print("You're on the waiting list.")
else:
   print("Keep up the good work.")

# ---------------------------------------------------------------------
# Exercise 4: Shopping Discount
# A store is offering a discount on a product. Write a program that
# takes the original price and the discount percentage as input.
# If the discounted price is less than $50, print "Great deal!".
# Otherwise, print "Might want to wait for a better offer."
original_price = float(input("Enter product original price: "))
discount_percentage = float(input("Enter discount percentage: "))

discounted_price = original_price * discount_percentage / 100 # calculate the discounted price here
final_price = original_price - discounted_price
if final_price > 50:
    print("Great deal!")
else:
    print("Might want to wait for a better offer.")

# <Your code here>

# ---------------------------------------------------------------------
# Exercise 5: Movie Night Decision
# You and your friends are deciding on a movie to watch. Write a
# program that takes two movie ratings as input. If both ratings
# are above 7, print "Let's watch both!". Otherwise,
# print "Let's just pick one."

movie_one = float(input("Enter movie rating for movie 1: "))
movie_two = float(input("Enter movie rating for movie 2: "))

if movie_one > 7 and movie_two > 7:
    print("Let's watch both!")
else:
    print("Let's just pick one.")

# ---------------------------------------------------------------------

# Exercise 6: Restaurant Recommendation
# You're building a restaurant recommendation system. Write a program
# that takes a person's mood (happy or sad) and hunger level
# (high or low) as input. If they're happy and hungry, recommend
# a fancy restaurant. If they're sad and hungry, recommend comfort food.
# For other cases, recommend a casual dining place.

# Inputs
mood = input("What is your mood? ")
hunger = input("What is your hunger? ")

# Define conditions
happy = 'happy'
sad = 'sad'
high_hunger = 'high'
low_hunger = 'low'

# Check recommendations
if mood == happy and hunger == high_hunger:
    print('I recommend a fancy restaurant.')
elif mood == sad and hunger == low_hunger:
    print('I recommend comfort food.')
else:
    print('I recommend a casual dining place.')

# ---------------------------------------------------------------------
# Exercise 7: Exercise 7: Tax Bracket Calculator
# You're building a tax calculation system. Write a program that
# takes a person's annual income as input. Use conditionals
# to determine their tax bracket based on the following rules:

# - If income is less than $40,000, tax rate is 10%.
# - If income is between $40,000 and $100,000 (inclusive), tax rate is 20%.
# - If income is greater than $100,000, tax rate is 30%.

# Remember that a tax rate of 10% can be represented as 10/100 or 0.1

# Print the calculated tax amount for the given income.
#annual_income = float(input("Enter your annual income: "))
annual_income = float(input("Enter your annual income: "))
#tax_rate = .1,.2,.3
tax_rate_1 = .1
tax_rate_2 = .2
tax_rate_3 = .3
tax_amount_1 = annual_income * tax_rate_1
tax_amount_2 = annual_income * tax_rate_2
tax_amount_3 = annual_income * tax_rate_3
if annual_income <= 40000:
    print(f"your annual income tax ${tax_amount_1}")
elif annual_income <= 100000:
    print(f"your annual income tax is ${tax_amount_2}")
else:
    print(f"your annual is ${tax_amount_3}")
#print(f"Your tax amount is ${tax_amount}")
# ---------------------------------------------------------------------
# Exercise 8: Ticket Pricing System
# You're working on a ticket booking system for an amusement park.
# Write a program that takes a person's age as input and determines
# their ticket price based on the following rules:
# - Children (ages 3 to 12): $10
# - Adults (ages 13 to 64): $20
# - Seniors (ages 65 and above): $15
# Print the calculated ticket price for the given age.

# <Your code here>
# Exercise 8: Ticket Pricing System
# You're working on a ticket booking system for an amusement park.
# Write a program that takes a person's age as input and determines
# their ticket price based on the following rules:
# - Children (ages 3 to 12): $10
# - Adults (ages 13 to 64): $20
# - Seniors (ages 65 and above): $15
# Print the calculated ticket price for the given age.

# <Your code here>
person_age = int(input("What is your age? "))
children_price = "Your ticket price is $10."
adults_price = "Your ticket price is $20."
seniors_price = "Your ticket price is $15."
baby_price = "Your baby is free!"
if person_age >= 65:
    print(seniors_price)
elif person_age >= 13:
    print(adults_price)
elif person_age >= 3:
    print(children_price)
else:
    print(baby_price)

# ---------------------------------------------------------------------
# Exercise 9: Password Strength Checker
# Create a program that takes a password as input and checks its
# strength based on the following rules:

# If the password is less than 8 characters, print "Weak password."
# If the password is 8 to 12 characters long, print "Moderate password."
# If the password is more than 12 characters, print "Strong password

# You can use len() function to get the length of a given string.

#password = input("Enter your password: ")

password = input("Enter your password: ")
password_1 = "Weak password"
password_2 = "Moderate password"
password_3 = "Strong password"
if len(password) > 12:
    print(password_3)
elif len(password) >= 8:
    print(password_2)
else:
    print(password_1)


# ---------------------------------------------------------------------
# CHALLENGE (OPTIONAL): Course Enrollment Eligibility
# To solve this exercise, you will need to use the following concepts
# and methods:
# - String method .upper()
# - String slicing
# - if-elif-else conditional statements
#
# You're designing a course enrollment system. Write a program that
# takes a course code and a student's grade as input and determines
# whether the student is eligible to enroll in the course.

# 1. Ask the user to enter a course code (e.g., "CS101", "MATH202", ).
#    All courses ends with "101", "202" or "303". Slice the string
#    to get the last three character of the string to get the course
#    ending:
#
#    Hint:
#    test = "ABCDEF"  # Given this string
#    print(test[-2:])  # It will print "EF"

# 2. Ask the user to enter their grade (e.g., "A", "B", "C", "D", "F").
#    Use .upper() method to convert the course code and grade to uppercase,
#    allowing for case-insensitive input.
#
# Implement the following enrollment rules:
# - For courses with course codes ending in "101", students with
#   grades "A" or "B" are eligible.
# - For courses with course codes ending in "202", students with
#   grades "B" or "C" are eligible.
# - For courses with course codes ending in "303", students with
#   grades "C" or "D" are eligible.

# Print either "You are eligible to enroll." or "You are not eligible to enroll."
course_code = input("Enter the course code: ")
student_grade = input("Enter your grade: ")

# Convert input to uppercase for case-insensitive comparison
course_code = course_code.upper()
student_grade = student_grade.upper()

# Extract the last three characters of the course code (use string slicing)
course_suffix =  # your code here

# Check course code and grade to determine eligibility
if course_suffix == "101":
    ...  # <Your code here>
elif course_suffix == "202":
    ...  # <Your code here>
# <Your code here>
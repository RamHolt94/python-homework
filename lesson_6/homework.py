# Task 1. Create three lists:

# List #1: Create an empty list and then use append() to populate it with the names of three of your friends.
# List #2: Create the same list, but use the syntax to create it pre-populated.
# List #3: Create the same list, but each element should be a list,
# where the first sub-element is the friend's name
# and the second sub-element is their age.

# List 1:
# list_1 = []
# list_1.a???('Friend1')
# list_1.???('Friend2')
# list_1.???('Friend3')

# List 2:
# list_2 = [???, ???, ???]

# List 3:
# list_3 = [
#     ???,
#     ???,
#     ???,
# ]
# List 1:
list_1 = []
list_1.append('John')
list_1.append('Fred')
list_1.append('King')
print(list_1)
# List 2:
list_2 = ["John", "King", "Fred"]
print(list_2)
# List 3:
list_3 = [
    'John',
    'Fred',
    'King',
    [23,
     27,
     30]
]
print(list_3)

# ---------------------------------------------------------------------
# Task 2. Retrieve elements from a List

# Create print statements to retrieve the following elements from the previous lists:
# - From List 2: Retrieve the name of the second friend.
# - From List 3: Retrieve the age of the last friend you put in the list.

# Name of second friend
second_friend_name = list_2[1]
print(second_friend_name)
# Age of the last friend of the list
last_friend_age = list_3[3][-1]
print(last_friend_age)
# ---------------------------------------------------------------------
# Task 3. Remove elements from a List

# From the lists provided, remove the requested elements. Easy peazy.

cities = ["Houston", "Dallas", "Austin"]
fruits = ["apple", "banana", "orange"]

# Remove Austin from cities without using its index
cities.remove("Austin")
print(cities)

# Remove the last element from fruits using negative indexes
del fruits[-1]
print(fruits)

# ---------------------------------------------------------------------
# Task 4. Verify if an element exists in a list

# Given the provided list, write code that prints `YES` if the list contains the word `cheese`

# The list
pantry = ["ham", "bread", "cheese"]

# Write code that prints YES if the list contains "cheese".

if "cheese" in pantry:
    print('YES')
else:
    print("cheese will not be on your sandwich")
#
# ---------------------------------------------------------------------
# Task 5. Sorting and Reversing

# Given the provided list, write code that sorts and reverses it, as required.

numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]

# Write code that sorts the list in ascending order without disturbing the original.
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Write code that reverses (flips) the list without disturbing the original.
# Remember that in this case, casting is required.
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)

# Write code that sorts the list in place, modifying the original.
numbers.sort()
print(numbers)

# Write code that reverses (flips) the list in place, modifying the original.
numbers.reverse()
print(numbers)

# ---------------------------------------------------------------------
# Task 6. Stitching and Slicing

# You are given two lists with names of days of the week:

# - `work_days` contains the work week days (Mon-Fri)
# - `rest_days` contains the weekend days (Sat-Sun)

# Create a third list that contains the _concatenation_ of the previous two.
# Call it 'full_week'

# Now, write python code that prints a slice from 'full_week' with the work days.

work_days = ['mon', 'tue', 'wed', 'thu', 'fri']
rest_days = ['sat', 'sun']

# Concatenate work_days and rest_rays
full_week = work_days + rest_days

# Slice with the work days
print(full_week[0:5])

# ---------------------------------------------------------------------
# Task 7. Aggregators and Helpers

# Given a list of numbers, use helpers and aggregators to answer the questions:

# - What's the lowest number?
# - What's the highest number?
# - What's the sum of all the numbers in the list?
# - How many times is the number 9 in the list?
# - How many total elements are in the list?

numbers = [6, 34, 17, 9, 2, 11, 57, 9, 32]
# Lowest number
print(min(numbers))

# Highest number
print(max(numbers))

# Sum of everything
print(sum(numbers))

# Count number 9s
print(numbers.count(9))

# Total number of elements
print(len(numbers))

## Exercises 🏋🏻

# ---------------------------------------------------------------------
# Exercise 1. The Biography Creator

# Create a program that will ask you for the following items and stores them in a list for later usage:

# - Your Name
# - Your Age
# - The name of the city where you were born

# The program should use a variable with a string that will be used as a template.
# This template should be a sentence that can be used to build the person's biography.

# Fox example:

# biography = "My name is <NAME>, I'm <AGE> years old and I was born in <CITY>."

# Tips:
# - Use f-strings with placeholders to build the actual template, with elements of the list as values.
# - Use input() to gather the data.
# - Use print() at the end, to show the user's biography.

# Declare an empty list
# user_data = []

# Gather user input
# name = input("Name: ")
# age = input("Age: ")
# city = input("City: ")

# Add user input to the list
# user_data.append(name)
# user_data.append(age)
# user_data.append(city)

# Declare your template. Use list elements as values.
# biography = f""

# Show the user's biography
# print(biography)
user_data = []
name = input('Enter your name: ')
user_data.append(name)
# print(name)
age = input('Enter your age: ')
user_data.append(age)
city = input('Enter the city your were born in: ')
user_data.append(city)

biography = (f"My name is {name}, I'm {age} years old and I was born in {city}.")
print(biography)

# ---------------------------------------------------------------------
# Exercise 2. The Card Deck ♦️♥️♠️♣️

# You will be provided with a couple lists that contain the cards for a card deck.
# One of the lists contains the numbers, and the other one contains the faces.

# You will be asked to fill in the blanks to print out certain cards for a card game you've been working on.

# 🔥 Tip: You might want to stitch them together first.

# # Here are the card decks.
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# faces = ['J', 'Q', 'K']
#
# # Concatenate them first.
card_deck = numbers + faces
#
# # Print out the numbers 1 to 6.
print(card_deck[0:6])
#
# # Print out the last 3. Do it using POSITIVE indexes.
print(card_deck[10:13])
#
# # Print out the last 3 (same as before), but using NEGATIVE indexes.
print(card_deck[-3:])
#
# # Print out everything EXCEPT the first and last.
print(card_deck[1:12])
#
# # What would you use so the printout includes the following:
# # Hint: It's every third card of the full deck.
# # ['1', '4', '7', '10', 'K']
print(card_deck[0:13:3])
#
# # Print out the EVEN numbers. No faces.
print(card_deck[9:0:-2])
# ---------------------------------------------------------------------
# Exercise 3. The Steps Tracker 👟

# Walking is a great way to improve one's health, and it can be fun!
# Doctors recommend 10,000 steps per day! You would like to know how many steps are YOU taking per day and per week.

# Write a program that will ask you the number of steps taken each day of the week, for one week.
# The program should put the step counts in a list, where index 0 is the number for Monday,
# index 1 is the number for Tuesday, and so on.

# Once you have all the steps counts, answer the following questions:
# - How many steps you took on Wednesday?
# - How many steps you took on the work days (Mon - Fri)?
# - How many steps total did you take over the whole week?
# - What was the least number of steps you took on a day?
# - What was the most number of steps you took on a day?
steps = []
monday = input('Steps for Monday: ')
steps.append(monday)
tuesday = input('Steps for Tuesday: ')
steps.append(tuesday)
wednesday = input('Steps for Wednesday: ')
steps.append(wednesday)
thursday = input('Steps for Thursday: ')
steps.append(thursday)
friday = input('Steps for Friday: ')
steps.append(friday)
saturday = input('Steps for Saturday: ')
steps.append(saturday)
sunday = input('Steps for Sunday: ')
steps.append(sunday)

# Steps on Wednesday
print(steps[2])

# Steps on the work days
work_days_steps = steps[0:5]
print(sum(work_days_steps))

# Steps over the whole week
whole_week_steps = steps[0:7]
print(sum(whole_week_steps))

# Least number of steps
print(min(steps))

# Highest number of steps
print(max(steps))

# ---------------------------------------------------------------------
# Exercise 4. Bonus Round: The Speech Reverser and Counter 🎤

# Python has a handy little method that allows you to split a string.
# In its most basic form it splits a string into a list using the spaces as separators:

# Example:

# phrase = "My Name is Joseph"
# words = phrase.split()
# print(words) -> ['My', 'Name', 'is', 'Joseph']

# More information about split: https://www.w3schools.com/python/ref_string_split.asp

# Now, armed with `split()` write a program that does the following:

# - Takes a string input from the user.
# - Splits it into words.
# - Prints out the string with the words in reverse order.
# - Prints out the word count.

# Get input from the user
user_input = input('Give me a phrase')

# Split user input into words
words = user_input.split()

# Reverse the list and print it
reversed_words = list(reversed(words))
print(reversed_words)

# Print the length of the words list
print(len(words))

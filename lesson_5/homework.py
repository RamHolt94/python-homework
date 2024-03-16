# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
#
# Create a variable called my_number and set it to any integer value.
# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.
#
# Example:
# Input: -3 => Output: 3
# Input: 5 => Output: 5

my_number = -5
if my_number >= 0:
    print(my_number)
else:
    print(my_number * -1)


# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
#
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”
number = int(input("Enter a number: "))
divisible_by_three = 'Bin'
divisible_by_seven = 'Go'
divisible_by_both = 'BinGo'
if number % 7 == 0 and number % 3 == 0:
    print(divisible_by_both)
elif number % 7 == 0:
    print(divisible_by_seven)
else:
    print(divisible_by_three)
# ---------------------------------------------------------------------

# Challenge 3
# Find the middle number
#
# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.
#
# Example:
# x = 1, y = 5, z = 3 => Output: 3
variable =[1, 6, 9]
x = 1
y = 6
z = 9

# if x < y :
#    print((f"{x} is the small number, keep looking!"))
# elif z > y:
#    print(f"{y} is the middle number you seek!")
# else:
#   print(f"{z} is not the number you seek!")

print(variable[1])

# ---------------------------------------------------------------------

# Challenge 4
# Palindrome Numbers
#
# Ask a user to input a number.
# Write a program to check if the given number is a palindrome.
# It should print True if the number is a palindrome and False if it is not.
#
# Palindrome number: 121, 898

numbers = input("Enter your number: ")
reversed_numbers = numbers[::-1]
if numbers == reversed_numbers:
    print("True")
else:
    print("False")


# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

word = "tcefreP!"
reversed_word = word[6::-1]
print(reversed_word + '!')


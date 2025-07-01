


# Abdelrhman Ahmed
# Software Developer
# Linkedin: https://www.linkedin.com/in/abdelrhman-ahmed-82609b296/




# What is Python?
# Python is a high-level, interpreted, and general-purpose
# programming language.
# It emphasizes readability, uses indentation to define blocks
# (object-oriented, and functional).

# 📜 History
# Created by: Guido van Rossum
# First released: 1991
# Current major version: Python 3 (Python 3.12 as of mid-2024)

# 🎯 Key Features

# Easy to read/write: Clean and simple syntax
# Interpreted: No need to compile before running
# Dynamically typed: No need to declare variable types
# Extensive libraries: From data science to web development
# Cross-platform: Runs on Windows, macOS, Linux, and more




# Install Python --> https://www.python.org/




# First Program

# print("Hello Python")






# Comments (This is a single line comment)

"""
This is a multi-line comment    
jhblbjklnlkjnlkn
kjbjkbkljbjlkb
bkjbkjnjk
"""







# \\	Backslash	    
# print("a\\b")	

# \'	Single quote	    
# print('It\'s ok')	

# \"	Double quote	   
# print("He said: \"Hi\"")	

# \n	New line	        
# print("Line1\nLine2")

# \t	Tab (horizontal) = 4 spaces
# print("Name:\tJohn")	                    

# \r	Carriage return (goes to line start)	
# print("Hello\rWorld")	

# \b	Backspace
# print("abc\b1")	

# \a	Bell/alert (may make a beep)	
# print("\a")	






# Variables --> Dynamic Typing

# name = "Abdelrhman"
# age = 25
# height = 1.75
# is_student = True






# | Type       | Example                    |
# | ---------- | -------------------------- |
# | `int`      | `x = 10`                   |
# | `float`    | `pi = 3.14`                |
# | `str`      | `name = "Ali"`             |
# | `bool`     | `is_valid = True`          |
# | `list`     | `nums = [1, 2, 3]`         |
# | `dict`     | `person = {"name": "Ali"}` |
# | `tuple`    | `coords = (4, 5)`          |
# | `set`      | `unique = {1, 2}`          |
# | `NoneType` | `x = None`                 |




# x = 3.14
# print(type(x))  # <class 'int'>


#  Variable Naming Rules

# Must start with a letter (A–Z or a–z) or an underscore _
# Can contain letters, digits, and underscores
# Case-sensitive (Age ≠ age)
# Cannot be a keyword (class, def, if, etc.)

# PI = 3.14159
# MAX_USERS = 100









# Arithmetic Operations

# | Operator       | Symbol | Example   | Result | Description                     |
# | -------------- | ------ | --------- | ------ | ------------------------------- |
# | Addition       | `+`    | `5 + 3`   | `8`    | Adds two numbers                |
# | Subtraction    | `-`    | `5 - 2`   | `3`    | Subtracts second from first     |
# | Multiplication | `*`    | `4 * 3`   | `12`   | Multiplies two numbers          |
# | Division       | `/`    | `10 / 4`  | `2.5`  | Returns a float                 |
# | Floor Division | `//`   | `10 // 4` | `2`    | Returns integer (no remainder)  |
# | Modulus        | `%`    | `10 % 4`  | `2`    | Returns remainder               |
# | Exponentiation | `**`   | `2 ** 3`  | `8`    | Raises first to power of second |



# x = 6
# y = 3
# x **= y
# print(x)

# | Symbol    | Equivalent To |
# | --------- | ------------- |
# | `x += y`  | `x = x + y`   |
# | `x -= y`  | `x = x - y`   |
# | `x *= y`  | `x = x * y`   |
# | `x /= y`  | `x = x / y`   |
# | `x //= y` | `x = x // y`  |
# | `x %= y`  | `x = x % y`   |
# | `x **= y` | `x = x ** y`  |

# x = 10
# y = 20
# x += y # x = 30
# y /= x # y = 0.666667
# x -= 2 * y # x = 30 - 1.3333333
# print(x, y)








# Input

# username = input("Please enter your username: ")
# print("hello" + username)







# Task - 1
# Write a program that calculate the discount of a product...


# int()
# float()
# str()

price = input("Please enter the product price: ")
price = int(price)
discount = input("please enter the discount value: ")
discount = float(discount)
print("the price after discount is : " + str(price - price*discount))


# Task - 2
# write a one-line calculator program
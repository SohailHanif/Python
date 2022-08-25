# Print result of addition and subtraction
print(1 + 2)
print(5 - 3)

# Print result of multiplication and division
print(2 * (3 + 4))
print(5 / 2)
print(6 / 2)
# Double slash division returns rounded integer
print(5 // 2)

# Operations with negative numbers
print(-5 + 2)
print(-3 * 4)

# Division by 0 with error
# print(5 / 0)

# Floats
print(3 / 4)
print(5 + 0.5)
print(0.1 + 0.2)

# Exponentiation
print(2 ** 5)
print(2 ** -3)

# Quotient, integer after division
print(9.5 // 3)

# Modulus, remainder after integer division
print (9.5 % 3)

# Strings
print("Hello World!")
print('Hello Python!')

# Escaping strings
print('Jane wanted to borrow John\'s car')
print("John said he: \n\t\"Would think about it\"")

# String Concatenation
print("Green eggs" + " " + "and ham")
print("3 eggs and ham cost: $" + str(10))
# print("3 eggs and ham cost: $" + 10)

# String multiplication
print("I don't need it\n" * 3)
print("I NEED IT")
print("1" + "0" * 9)

# Type conversions
print(str(2) + str(3))
print(float(2) + float(3))
print(int("2") + int("3"))

# Variables
x = 5
print(x + 3)
print(x)
print(type(x))
x = "x is a string now"
print(x + "!")
print(type(x))


# Variable names
this_is_a_normal_variable_name = 3
# 123abc = 2

# Deleting variables
num_clicks = 7
print("Number of clicks: " + str(num_clicks))
num_clicks = None
print("Number of clicks: " + str(num_clicks))
del num_clicks
# print(num_clicks)

# In-place operators
y = 8
y += 4
print(y)
y /= 4
print(y)

order = "Bread"
order += " and butter\n"
print(order)
order *= 3
print(order)

# Multiple variable assignment and output
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

"""
This is a multline comment
Used for multiline strings
"""
multiline_text = """
This is my
multiline text
"""
print(multiline_text)

# String formatting
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old")

# String methods and formatting
print(f"My name is {name.upper()} and I am {str(age).replace('3', '2')} years old")
print(f"Formatted float addition {(0.1 + 0.2):0.2f} vs Unformatted {0.1 + 0.2}")
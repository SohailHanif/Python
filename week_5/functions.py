# Declare function
def my_func():
    print("apple")
    print("banana")
    print("orange")

# Call function
my_func()

# Function that accepts 1 argument
def print_with_exclamation(word):
    print(f"{word}!")

# Call function with different arguments
print_with_exclamation("Hello")
print_with_exclamation("apple")
print_with_exclamation("python")

# Create function that accepts 2 arguments
def print_sum(x, y):
    print(f"Sum of {x} and {y} is {x + y}")

print_sum(5, 8)

def print_var(x):
    x += 1
    print(x)

print_var(7)
# Trying to access variable outside scope
# print(x)

# Function that returns value
def max(x, y):
    if x >= y:
        return x
    else:
        return y

# Print value returned from function
print(max(4, 7))
# Assign value to variable
z = max(8, 5)
print(z)

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4, 5))

def multiply(x, y):
    return x * y
a = 4
b = 7
# Assign function to var
operation = multiply
print(type(operation))
print(operation(a, b))

def add(x, y):
     return x + y
# Function that accepts function as parameter
def do_twice(func, x, y):
      return func(func(x, y), func(x, y))
a = 5
b = 10

print(do_twice(add, a, b))

# Create lambda that double the argument entered
double = lambda x: x * 2
print(double(5))

# Lambda that adds 2 numbers together
f = lambda x, y: x + y
print(f(1, 1))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Call map with lambda as argument
new_numbers = list(map(lambda x: x * 2, numbers))
print(new_numbers)

# Filter function to filter for even number using lambda
even_numbers = list(filter(lambda x: (x % 2 == 0), numbers))
print(even_numbers)

# Import random module
import random

for i in range(5):
    # Get random number using module
    value = random.randint(1, 6)
    print(value)

# Import variable instead of entire module
from math import pi
print(pi)

# Import multiple variables/functions from module
from math import pi, sqrt
from random import *

print(sqrt(81))
print(randint(10, 100))

# Use rename on import
from math import sqrt as square_root
print(square_root(100))

# Import module installed using pip
from termcolor import colored
print (colored('hello', 'blue'), colored('world', 'green'))
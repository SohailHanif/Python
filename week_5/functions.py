from random import randint
from math import *
from termcolor import colored

def my_func():
    print("apple")
    print("banana")
    print("orange")

def print_with_exclamation(word):
    print(f"{word}!!!!!")

def print_inc_num(x):
    x += 1
    print(x)

def max(x, y):
    if x>y:
        return x
    else:
        return y

def multiply(x,y):
    return x*y

def do_twice(func, x, y):
    x += 1
    y += 2
    
    print(multiply(func(x, y), func(x, y)))

double = lambda x: x * 2
triple = lambda x: x * 3
add = lambda x, y, z, a, b: x + y + z+ a +b

numbers = [ 1, 3, 10, 20, 4, 6, 2]
new_numbers = list(map(lambda num: num * 5, numbers))
even_numbers = list(filter(lambda num: (num % 2 == 0), numbers))

print(colored("Hello", "green"), colored("World", "blue"))
# print(pi)
# print(sqrt(100))

# for i in range(10):
#     print(randint(10, 100))


# print(numbers)
# print(new_numbers)
# print(even_numbers)

# print(double(5))
# print(triple(5))
# print(add(10, 20, 4, 6, 2))




# a = 2
# b = 3
# do_twice(multiply, a, b)
# print(a)
# print(b)



# operation = multiply
# print(multiply)
# print(operation)
# print(type(operation))
# print(operation(a,b))
# largest_num = max(a, b)


# print_with_exclamation("Python")
# print_with_exclamation("is")
# print_with_exclamation("fun")

# x = 5
# print_inc_num(x)
# print(x)


wins = 10
losess= 1

def reset_wins():
    global wins
    global losess
    wins = 0
    losess = 0

print(wins)
reset_wins()
print(wins)

def generate_random_num():
    min_num = int(input("Enter min num"))
    max_num = int(input("Enter min num"))

    rand_num = randint(min_num, max_num)
    return rand_num
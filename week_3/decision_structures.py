# Create boolean variable
my_boolean = True
print(my_boolean)

# Comparison == returns boolean result
print (2 == 3)
print("hello" == "hello")

# Comparison with not equal operator
print(1 != 1)
print("hello" != "goodbye")
print(2 != 3)

# Comparison with greater and less than operators
print(7 > 5)
print(10 < 20)
print(2 > 3)
print(10 < 10)

# Comparison with greater and less than or equal to operators
print(9 >= 9.0)
print(7 <= 10)
print(2 >= 3)
print("abc" >= "def")
print("ebc" >= "def")

# Boolean casting different data types
print(bool("hello"))
print(bool(10))
print(bool(1))
print(bool(0))
print(bool(""))
print(bool(None))

# If statements
if (10 > 5):
    print("If true this code is executed")

print("This code is executed regardless")

x = 4
y = 2
if (x > y):
    print(f"{x} is greater than {y}")

# Nested if statements
num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 100:
        print("Between 5 and 100")

# Else condition
x = 4
y = 20
if (x >= y):
    print(f"{x} is greater than or equal to {y}")
else:
    print(f"{y} is greater than {x}")

# Elif condition
x = 4
y = 4
if (x > y):
    print(f"{x} is greater than {y}")
elif (x == y):
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is less than {y}")

# num = 3
if num == 5:
    print("Number is 5")
elif num == 11:
    print("Number is 11")
elif num == 7:
    print("Number is 7")
else:
    print("Number isn't 5, 11 or 7")

# Boolean AND
if(1 == 1 and "hello" == "hello"):
    print("Both statements are True")

print(1 == 1 and 2 == 3)
print(1 == 1 and "hello" == "goodbye")
print(1 != 1 and 2 == 2)
print(3 > 1 and 2 < 5)
print(1 == 1 and 2 != 3)

# Boolean OR
if(1 == 1 or "hello" == "hello"):
    print("Both statements are True")

print(1 == 1 or 2 == 3)
print(1 == 2 or "hello" == "goodbye")
print(1 != 1 or 2 == 3)
print(3 < 1 or 2 < 5)
print(1 == 2 or 2 != 3)

# Boolean NOT
print (1 == 1)
print (not 1 == 1)
print (not 2 > 1)

# Order precedence
print(False == False or True)
print(False == (False or True))
print((False == False) or True)

# While loop
i = 1
while(i <= 5):
    print(i)
    i += 1

# Infinite loop
# while 1==1:
#     print("In the loop")

# Break infinite loop
i = 1
while True:
    print(i)
    i += 1
    if (i > 5):
        break
print("Out of the loop")

# Continue Loop
i = 0
while i <= 5:
    i += 1
    if i == 2 or i == 4:
        print("Skipping 2 and 4")
        continue
    print(i)

# Input
x = int(input("Enter a number: "))
print(f"Number inputted is {x}")

# Exercise
while True:
    # Get numbers from input and cast as float
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    # Compare using if/elif/else to determine which number is bigger
    if (num1 > num2):
        # Output using interpolated f-string
        print(f"The first number({num1}) is greater than the second number({num2})")
    elif (num1 == num2):
        print(f"The two numbers are equal({num1})")
        # Continue starts from top of loop and does not allow to exit program if equal
        continue
    else:
        print(f"The second number({num2}) is greater than the first number({num1})")

    # Get user input to determine if exiting program or continuing
    continue_loop = input("Do you want to continue? (y/n): ")
    # Use lower string method to compare
    if (continue_loop.lower() == "n"):
        print("Exiting program...")
        # Use break to exit infinite loop
        break

# Trigger ZeroDivisionError Exception
# print(4/0)

# Trigger ModuleNotFoundError
# import invalid_package

# Using variable that doesn't exit
# Results in NameError
# print(my_list)

# Trigger IndexError by accesing index that doesn't exist
my_list = [1, 2, 3]
# print(my_list[4])

# Trigger sytax exception by having code that can't be parsed
print(my_list)
# print my_list

# TypeError occurs when trying to use operator with invalid types
# print("hello" + 5)

# ValueError occurs when function is called on correct type but invalid vlaue
print(int("21"))
# print(int("cat"))

# Exception handling with try/catch block
try:
    print(5/0)
except:
    print("An exception occured")

print("Program execution not stopped")

# Exception handling with try/catch
try:
    num = 10
    # Throws TypeError
    print(num + "hello")
    # Throws ZeroDivisionError
    print(num / 0)

# Catch ZeroDivisionError error 
except ZeroDivisionError:
    print("Divided by zero")

# Catch ValueError or TypeError
except (ValueError, TypeError):
    print("Error occurred")


# Exception handling with try/catch
try:
    num = 10
    # Throws TypeError
    print(num + "hello")
    # Throws ZeroDivisionError
    print(num / 0)

# Catch ZeroDivisionError error 
except ZeroDivisionError:
    print("Divided by zero")

# Catch ValueError or TypeError
except (ValueError, TypeError):
    print("Error occurred")

try:
    my_list = [1, 2, 3]
    print(my_list[4])
# Catch error object as error
except Exception as error:
    print(error)
# Finally is run after try or excpet is finished
finally:
    print("Runs regardless")
print("Still executed")

print(1)
# Raise error with message
# raise ValueError("Error with custom message")
print(2)

try:
    num = 5 / 0
except:
    print("An error occurred")
    # Re-raise error
    # raise
print("Not executed")

print(1)
# Create assertion
assert 2 + 2 == 4
print(2)
# assert 1 + 1 == 3
# print(3)

temp = int(input("What is the temperature?: "))
assert (temp >= 0), "Too cold!"

# Open file for reading
file = open("exceptions.py")
print(file)
# Read file contents
print(file.read())

try:
    file = open("exceptions.py", "r+")
    # Read limited file contents, moves cursor
    print(file.read(37))
    # Continue from where previous read left off
    # Print next 3 lines
    print(file.readlines(3))
except:
    print("An error occured")
# # Always executed
finally:
    # Close the file
    file.close()
    print("Closed the file")


# Writing files
try:
    # Open newfile in write mode
    file = open("newfile.txt", "w")
    # Write contents of file
    file.write("This has been written to a file")
    file.close()
except:
    print("Exception occured")
finally:
    file.close()

# Use with instead of try/catch/finally
# Open file for appending
with open("newfile.txt", "a") as f:
    # Append content to file
    f.write("\nAppended to file")

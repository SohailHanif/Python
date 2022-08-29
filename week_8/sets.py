# Create set using {}
num_set = {1, 2, 3, 4, 5}
# Create set using set()
word_set = set(["spam", "eggs", "sausage"])

print(num_set)
print(word_set)

# Create empty set
empty_set = set()
# Get len of sets
print(len(word_set))
print(len(empty_set))
# Get if value is in set
print("eggs" in word_set)
print("eggs" in empty_set)

# Try to create duplicate set
duplicate_set = set([1, 2, 3, 3, 4, 2])
print(duplicate_set)
# Try to get set value by index
# print(num_set[1])

# print(num_set)
num_set.add(10)
num_set.remove(3)
num_set.pop()
print(num_set)

# Math operators on sets
# Union operator | combines sets
print(num_set | word_set)
# Difference operator - gets item in first set but not second
print(num_set - duplicate_set)
# Intersection operator & gets items in both
print(num_set & duplicate_set)
# Symmetric operator ^ gets items in one set but not both
print(num_set ^ duplicate_set)

# Create new tuples
num_tuple = (1, 2, 3)
word_tuple = "apple", "banana", "orange"

print(num_tuple)
print(word_tuple)
print(type(word_tuple))

# Access tuple by index
print(word_tuple[1])
# word_tuple[1] = "cherry"

empty_tuple = ()
mixed_tuple = (1, "hello", 3.14)

print(empty_tuple)
print(type(empty_tuple))
print(mixed_tuple)


nested_tuple = (1, 2, (3, 4, 5), 6.5)

print(nested_tuple)
# # Nested index
print(nested_tuple[2][1])

packed_tuple = "a", 4.6, "cat"
# Unpack tuple to vars
a, b, c = packed_tuple
print(a)
print(b)
print(c)

tuple_with_list = (1, 2, [3, 4], 5, 6)
print(tuple_with_list[2])
# Update value of list value in tuple
tuple_with_list[2][1] = 7
print(tuple_with_list[2])
# Reassign tuple
tuple_with_list = ([1, 2], [3, 4, 5])
print(tuple_with_list)

# Concatenate tuple
print((1, 2, 3) + (4, 5, 6))

# Multiply tuples
print(("Repeat", "this", "text") * 3)

temp_tuple = (1, 2, 3)
# Delete entire tuple
del temp_tuple
temp_tuple = (1, 2, 3)
print(temp_tuple)
# Try deleting element in tuple
# del temp_tuple[1]

value_tuple = ("hello", "apple", "cherry")
print("apple" in value_tuple)
print("banana" in value_tuple)
print("banana" not in value_tuple)

duplicate_tuple = (1, 2, 2, 4, 5, 4)
print(duplicate_tuple)
# Search for index of value
print(duplicate_tuple.index(5))
# Return number of elements in tuple matching value
print(duplicate_tuple.count(4))
# Get count of element that doesn't exist
print(duplicate_tuple.count(3))
# Get index of element that doesn't exist
# print(duplicate_tuple.index(3))

loop_set = {1, 3, "hello", 7.5}
loop_tuple = (1, 2, "goodbye", 9.5)

# Loop through set to get values
for element in loop_set:
    print(element)

# Loop through tuple to get vlaues
for element in loop_tuple:
    print(element)

# List comprehension
# Create list of numbers from 1-1 squared
squared_numbers = [i**2 for i in range(11)]
print(squared_numbers)

# # Create list of even numbers by using conditions
even_numbers=[i for i in range(100) if i % 2 == 0]
print(even_numbers)

# Memory error as value too large to store in memory
# even_numbers_large = [i for i in range(1000 ** 10000)]

# Create variable with value and type of none
a = None
print(a)
print(type(a))

# Trying to assign a value to a function that
# does not return a value is equal to None
functin_val = print("Print function does not return a value")
print(functin_val)
print(type(functin_val))

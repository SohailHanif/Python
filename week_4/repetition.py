# # Create new list
fruits = ["apple", "banana", "orange"]
# Print list element by index
print(fruits[0])
print(fruits[1])
print(fruits[-1])

# # Create empty array
empty_array = []
# Mixed variable types
mixed_array = ["Hello", 1, True, 2]
print(empty_array)
print(mixed_array)

# # Nested array
nested_array = [1, 2, [3, 4, 5], 6]
print(nested_array)
print(nested_array[2])

# # String character accessed by index
text = "Hello"
print(text[4])

# # List index update value
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

# # List concatenation and multiplication
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# Get elements after index 4
print(fruits[4:])
# Get elements before and including index 6
print(fruits[:5])

# In operator list
words = ["spam", "egg", "spam", "toast"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

# In operator substring
text = "Hello World!"
print("World" in text)

# # Check if values not in list and text
print("tomato" not in words)
print(not "tomato" in words)
print("World" not in text)
print("a" not in text)

empty_array = []
value_array = [1, 2, 3]
# Append elements to end of array
empty_array.append(1)
value_array.append(4)

print(empty_array)
print(value_array)

# Print length of array
print(len(empty_array))
print(len(value_array))
# Access index that doesn't exist
# print(empty_array[2])

# Use insert function to add
# text in the middle of list
words = ["Python", "fun"]
words.insert(1, "is")
print(words)

# Get index of searched items in array
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
# print(letters.index('z'))

# Examples of other functions
nums = [1, 2, 3, 4, 6, 7, 8, 0, 9, 2, 1]
print(f"Max: {max(nums)}")
print(f"Min: {min(nums)}")
print(f"Number of 2s: {nums.count(2)}")

nums.sort()
print(f"Sorted Nums: {nums}")
nums.reverse()
nums.remove(3)
nums.pop(1)
print(f"Reversed/removed Nums: {nums}")

# Range function
number_range = range(10)
print(number_range)
print(list(number_range))

# # One argument returns range from 0 to argument
numbers = list(range(8))
print(numbers)
# Range between arguments
numbers = list(range(3, 8))
print(numbers)

# Range from 5 to 20 in intervals of 2
numbers = list(range(5, 20, 2))
print(numbers)

# While loop to iterate over list
words = ["hello", "bye", "see you", "later"]
length = len(words)
i = 0
while (i < length):
    print(f"{words[i]}!")
    i += 1

# For loop to iterate list
for word in words:
    print(f"{word}!")

# Iterate over string
for character in "Hello!":
    print(character)

# For loop with range
for num in range(5):
    print(num)

# # Nested list
fruit_cup_box = [["apple", "banana", "cherry"], ["orange", "kiwi"], ["melon", "mango"]]
# Iterate over top list
for fruit_cup in fruit_cup_box:
    print(f"Fruit Cup: {fruit_cup}")
    # Iterate over inner lists
    for fruit in fruit_cup:
        print(f"Fruit: {fruit}")
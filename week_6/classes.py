# # Define cake class
class Cake:
    # set attribute of class
    num_eggs = 3

# Create new cake object
cake = Cake()
# Get and print object property
print(cake.num_eggs)

class Person:
    # Run when object created
    def __init__(self, name, age):
        # set attribute of class to arguments
        self.name = name
        self.age = age

    # Method to print name and age
    def greeting(this):
        # self is automatically passed and renamed as this
        print(f"Hi, my name is {this.name} and I am {this.age}")


# Create person objects
person_1 = Person("John", 25)
person_2 = Person("Jane", 27)

# Get and print object property
print(person_1.age)
print(person_2.age)

# # Use object method to print greeting
person_1.greeting()
person_2.greeting()

# Update obejct property
person_1.age = 30
person_1.greeting()

# Delete object property
del person_1.age
# person_1.greeting()

# Delete entire object
del person_1
# person_1.greeting()


# Create class
class Student(Person):
    # Override parent init
    def __init__(self, name, age, school):
        # Inherit parent class using super
        super().__init__(name, age)
        self.school = school
        # Dictionary to store grades
        # Courses are keys, grades are values
        self.grades = {
            "Python": 98,
            "JavaScript": 95,
            "C": 85
        }

    # Override parent greeting method
    def greeting(self):
        print(
            f"Hi, my name is {self.name}, "
            f"I am {self.age} and go to {self.school}")


# Create student object
student_1 = Student('Jason', 21, "Humber")

# Use child class method
student_1.greeting()

# Use parent class method with super
super(Student, student_1).greeting()

# Print student grades
print(student_1.grades)
# Access dictionary using key to get value
print(student_1.grades["JavaScript"])
# Print number of elements in grades
print(len(student_1.grades))
# Print type of grades
print(type(student_1.grades))
# Print first key in dict (Python 3.7+ only)
print(list(student_1.grades)[0])
# Print first value in dict (Python 3.7+ only)
print(list(student_1.grades.values())[0])

# Get dictionary value using get method
print(student_1.grades.get("Python"))
# Print all keys
print(student_1.grades.keys())
# Create new key value pair
student_1.grades["C++"] = 90
# Get new value with key
print(student_1.grades.get("C++"))
# Show updated dictionary keys
print(student_1.grades.keys())
# Try to get key that doesn't exist with get()
print(student_1.grades.get("C+++"))
# Try to get key that doesn't exist directly
# print(student_1.grades["C+++"])

# Update value directly
student_1.grades["C++"] = 91
# Print dictionary as list of tuples
print(student_1.grades.items())
# Pass key value pair to update
student_1.grades.update({"C++": 92})
# Delete key from dict
student_1.grades.pop("C")
print(student_1.grades)
print("Hello, world!\n")

# Variables and data types Variables are used to store data in memory. 
# In Python, you don't need to declare the data type of a variable explicitly.
# Python automatically determines the data type based on the value assigned to the variable
my_name = "Mohammed"
my_age = 20
is_student = True

print("My name is", my_name)
print("I am", my_age, "years old")
print("I am a student:", is_student)


# Control flow and functions Control flow statements are used to execute code conditionally or repetitively. 
# Functions are used to encapsulate a block of code and reuse it whenever needed.
def print_hello():
    print("Hello!")

def print_greeting(name):
    print("Hello,", name)

print_hello()
print_greeting("John")

if my_age > 18:
    print("You are an adult.\n")
else:
    print("You are a minor.\n")

#Lists are used to store multiple values in a single variable. 
# Each value in a list is separated by a comma and enclosed in square brackets. Lists can contain values of different data types.
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
print(len(fruits))

fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits,"\n")

#Loops are used to execute a block of code repeatedly. There are two types of loops in Python: for loops and while loops.
for fruit in fruits:
    print(fruit)

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
print("\n")

#Dictionaries are used to store key-value pairs. Each key in a dictionary is associated with a value, 
# and the key-value pairs are separated by colons and enclosed in curly braces.
student = {
    "name": "John",
    "age": 30,
    "is_student": True
}

print(student)
print(student["name"])
print(len(student))

student["age"] = 31
print(student)

del student["is_student"]
print(student,"\n")


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
    print("You are an adult.")
else:
    print("You are a minor.")

# Python Assignment
# Topic: Variables, Data Types, and Control Structures

# -----------------------------------------
# Question 1: Variables and Data Types
# -----------------------------------------

# a) Create variables to store name, age, and favorite programming language.
name = "Yash"
age = 21
favorite_language = "Python"

# b) Print each variable along with a descriptive message.
print("Question 1: Variables and Data Types")
print("My name is", name)
print("I am", age, "years old.")
print("My favorite programming language is", favorite_language)


# -----------------------------------------
# Question 2: Control Structures
# -----------------------------------------

print("\nQuestion 2: Control Structures")

# a) Ask the user to enter an integer and check whether it is even or odd.
number = int(input("Enter an integer to check whether it is even or odd: "))

if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")

# b) Ask the user to enter a number and check whether it is positive,
# negative, or zero.
number = float(input("Enter a number to check whether it is positive, negative, or zero: "))

if number > 0:
    print(number, "is a positive number.")
elif number < 0:
    print(number, "is a negative number.")
else:
    print("The number is zero.")

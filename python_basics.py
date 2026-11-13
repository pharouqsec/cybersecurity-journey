"""
Python Basics Practice
A beginner-friendly reference covering the core building blocks of Python.
Run with: python python_basics.py
"""

# 1. VARIABLES
name = "Cybersecurity Learner"
study_hours = 2
is_learning_python = True

print("Name:", name)
print("Study hours:", study_hours)
print("Learning Python:", is_learning_python)


# 2. BASIC DATA TYPES
age = 20                 # integer (int)
progress = 75.5          # decimal (float)
course = "Python"        # text (str)
is_complete = False      # Boolean (bool)

print(type(age), type(progress), type(course), type(is_complete))


# 3. TYPE CONVERSION
number_as_text = "10"
number = int(number_as_text)
print("Converted number:", number)


# 4. OPERATORS
first_number = 12
second_number = 5

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Remainder:", first_number % second_number)


# 5. USER INPUT
# Uncomment these lines when you want the program to ask questions.
# user_name = input("What is your name? ")
# print("Welcome,", user_name)


# 6. CONDITIONALS: if, elif, else
score = 72

if score >= 80:
    print("Excellent result")
elif score >= 50:
    print("You passed")
else:
    print("Keep practising")


# 7. LISTS: ordered, changeable collections
topics = ["Networking", "Linux", "Python"]
topics.append("Cybersecurity")
print("Topics:", topics)
print("First topic:", topics[0])


# 8. TUPLES: ordered, unchangeable collections
operating_systems = ("Windows", "Linux", "macOS")
print("Operating systems:", operating_systems)


# 9. SETS: collections of unique values
protocols = {"HTTP", "DNS", "HTTP", "SSH"}
print("Unique protocols:", protocols)


# 10. DICTIONARIES: key-value pairs
student = {
    "name": "Alex",
    "track": "Blue Team",
    "level": "Beginner"
}
print("Student name:", student["name"])
print("Student details:", student)


# 11. FOR LOOP: repeat once for each item
print("Studying these topics:")
for topic in topics:
    print("-", topic)


# 12. WHILE LOOP: repeat while a condition is true
count = 1
while count <= 3:
    print("Practice attempt:", count)
    count += 1


# 13. LOOP CONTROL: break and continue
for number in range(1, 6):
    if number == 2:
        continue  # Skip 2
    if number == 5:
        break     # Stop before printing 5
    print("Number:", number)


# 14. FUNCTIONS: reusable blocks of code
def greet(person):
    return "Hello, " + person

message = greet("learner")
print(message)


# 15. FUNCTION WITH A DEFAULT PARAMETER
def describe_skill(skill, level="Beginner"):
    print(skill, "level:", level)

describe_skill("Python")
describe_skill("Networking", "Developing")


# 16. LIST COMPREHENSION: build a list in one line
numbers = [1, 2, 3, 4, 5]
squared_numbers = [number ** 2 for number in numbers]
print("Squares:", squared_numbers)


# 17. EXCEPTION HANDLING: handle expected errors safely
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("The calculation section has finished.")


# 18. FILE HANDLING: write to and read from a text file
# This creates a small text file in the same folder as this script.
with open("python_notes.txt", "w", encoding="utf-8") as file:
    file.write("I am learning Python step by step.\\n")
    file.write("I am practising for defensive cybersecurity.\\n")

with open("python_notes.txt", "r", encoding="utf-8") as file:
    notes = file.read()

print("Saved notes:")
print(notes)


# 19. MODULES: use functionality from Python's standard library
import datetime

today = datetime.date.today()
print("Today's date:", today)


# 20. MAIN ENTRY POINT
def main():
    print("Python basics practice completed.")

if __name__ == "__main__":
    main()

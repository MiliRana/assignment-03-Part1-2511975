# part1_grade_tracker.py
# Assignment 3 – Student Grade Tracker
# Name: Mili Rana
# Student ID: 2511975

# -------------------------------
# Task 1 – Data Parsing & Profile Cleaning
# -------------------------------

# creating a dictionary inside list
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# this loop will run for each student
for student in raw_students:
    # cleaning name and roll
    name = student["name"].strip().title()
    # roll no. is converted to integer
    roll = int(student["roll"])
    # this is list
    marks = [int(m) for m in student["marks_str"].split(", ")]

    # checking if name is valid (only alphabets)
    # if any name conatains numbers or symbols, it says invalid names
    valid = True
    for word in name.split():
        if not word.isalpha():
            valid = False

    if valid:
        print(name, "✓ Valid name")
    else:
        print(name, "✗ Invalid name")

    #this will give profile card of a student
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

    # special case for roll 103
    if roll == 103:
        print(name.upper())
        print(name.lower())


# -------------------------------
# Task 2 – Marks Analysis Using Loops & Conditionals
# -------------------------------

#marks analysis
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

#this is loop through subjects using index and get marks for that subject
for i in range(len(subjects)):
    m = marks[i]
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"
    print(subjects[i], "-", m, "-", grade)

#totals and averages
total = sum(marks)
average = round(total / len(marks), 2)
print("Total Marks:", total)
print("Average Marks:", average)

highest = max(marks)
lowest = min(marks)
print("Highest Scoring Subject:", subjects[marks.index(highest)], highest)
print("Lowest Scoring Subject:", subjects[marks.index(lowest)], lowest)

#using while loop for new subjects and entring marks for those subjects
print("\nEnter new subjects and marks (type 'done' to stop)")
new_count = 0
while True:
    subject = input("Enter subject name: ")
    if subject.lower() == "done":
        break

    marks_input = input("Enter marks: ")
    if not marks_input.isdigit():
        print("Invalid marks. Please enter a number.")
        continue

    marks_input = int(marks_input)
    if marks_input < 0 or marks_input > 100:
        print("Marks must be between 0 and 100.")
        continue

    subjects.append(subject)
    marks.append(marks_input)
    new_count += 1

#updated average
new_total = sum(marks)
new_average = round(new_total / len(marks), 2)
print("New subjects added:", new_count)
print("Updated Average Marks:", new_average)


# -------------------------------
# Task 3 – Class Performance Summary
# -------------------------------

#this is the list of tuples
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

#table header
print("Name              | Average | Status")
print("----------------------------------------")

#counters and list for averages.
pass_count = 0
fail_count = 0
averages = []

#will loop through each student
for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    averages.append(avg)

    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    print(f"{name:<18} | {avg:>6} | {status}")
    print()

print("Students Passed:", pass_count)
print("Students Failed:", fail_count)

top_avg = max(averages)
topper_index = averages.index(top_avg)
topper_name = class_data[topper_index][0]
print("Class Topper:", topper_name, "-", top_avg)

class_avg = round(sum(averages) / len(averages), 2)
print("Class Average:", class_avg)


# -------------------------------
# Task 4 – String Manipulation Utility
# -------------------------------

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

#will remove spaces from start and end
clean_essay = essay.strip()
print("Stripped Essay:")
print(clean_essay)
print()

#conerts into title case
title_essay = clean_essay.title()
print("Title Case Essay:")
print(title_essay)
print()

#it counts how many times the word python appears
count_python = clean_essay.count("python")
print("Number of times 'python' appears:", count_python)
print()

#replaces the word python with the snake
replaced_essay = clean_essay.replace("python", "Python 🐍")
print("Replaced Essay:")
print(replaced_essay)
print()

#it will split sentences into essay lists
sentences = clean_essay.split(". ")
print("Sentences List:")
print(sentences)
print()

#looping with numbers starting from 1
print("Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence += "."
    print(i, "-", sentence)

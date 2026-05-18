# Student Tracker System

# STUDENT GRADE TRACKER

english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))
maths = int(input("Enter Maths marks: "))
islamiat = int(input("Enter Islamiat marks: "))
pak_studies = int(input("Enter Pak Studies marks: "))

# total marks
total = english + science + maths + islamiat + pak_studies

# average
average = total / 5

# display result
print(" YOUR RESULT ")
print(f"Total Marks: {total}/500")
print(f"Average: {average}/100")

# grade system
if average >= 90:
    print("Grade: A (Excellent)")
elif average >= 80:
    print("Grade: B (Good)")
elif average >= 70:
    print("Grade: C (Satisfactory)")
elif average >= 60:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail - Need Improvement)")
# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

mark_scored=float(input("Enter the marks scored: "))
if mark_scored>=90:
    grade="A"
    print("grade",grade)
elif mark_scored>=80:
    grade="B"
    print("grade",grade)
elif mark_scored>=70:
    grade="C"
    print("grade",grade)
elif mark_scored>=60:
    grade="D"
    print("grade",grade)
elif mark_scored>=40:
    grade="E"
    print("grade",grade)
else:
    print("grade F")


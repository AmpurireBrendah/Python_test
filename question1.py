# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).
import math
squareroot=math.sqrt
x1=input("Enter the number: ")
x2=input("Enter the number: ")
y1=input("Enter the number: ")
y2=input("Enter the number: ")

first_point=(x1,y1)
second_point=(x2,y2)
distance=squareroot((x2-x1)**2+(y2-y1)**2)
print(f"The distance between two coordinate points {first_point} and {second_point} is : str({distance})")






# Question 1(ii)
# Write a Python program to find maximum between three numbers.
num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
num3=input("Enter the third number: ")
maximum_number=max(num1,num2,num3)
print(f"The maximum number between {num1}, {num2} and {num3} is :{maximum_number}")




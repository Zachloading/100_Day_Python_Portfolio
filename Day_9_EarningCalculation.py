"""
Date: 2/6/25
By: Zakareeya Amra
Goal: Create a program that calculates earnings. 
"""

#var
name = input (" Please Enter your Full name:")
hours = eval(input("Enter hours worked:"))
RPH = eval(input("Enter rate per hour: "))
Earnings = RPH * hours
#function
print("Hello,", name)
print("You have earned:$",Earnings)
print("Have a nice day!")

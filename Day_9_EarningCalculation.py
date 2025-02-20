"""
Date: 2/6/25
By: Zakareeya Amra
Goal: Create a program that calculates earnings. 
"""
name = input("Please Enter your Full Name: ")
hours = float(input("Enter hours worked: "))
RPH = float(input("Enter rate per hour: "))

# Calculate earnings with overtime pay
if hours > 40:
    overtime_hours = hours - 40
    regular_pay = 40 * RPH
    overtime_pay = overtime_hours * (RPH * 1.5)
    gross_earnings = regular_pay + overtime_pay
else:
    gross_earnings = hours * RPH

# Apply 7% tax
tax = gross_earnings * 0.07
net_earnings = gross_earnings - tax

# Output
print("Hello,", name)
print("You have worked", RPH, "hours")
print("Gross Earnings: $", format(gross_earnings, ".2f"))
print("Net Earning: $", format(net_earnings, ".2f"))
print("Have a nice day!")

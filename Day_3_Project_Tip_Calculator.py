#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Tip Calculator")
print("This App was built by Zakareeya Amra")
total = input("What was the total bill? $")
people = input("How many people split the bill? ")
percent = input("What percent tip would you like to leave? 10, 12, or 15 percent ? ")

if percent == '10':
  percent = '1.10'

if percent == '12':
  percent = '1.12'
 
if percent == '15':
 percent = '1.15' 

total_input = float(total)
people_input = float(people)
percent = float(percent)

result = (total_input / people_input) * (percent)
result = round(result, 2)
x = result
final_tip_amount = x
final_tip_amount_f = str(final_tip_amount)
print("Each person should pay:" + " " + "$" + final_tip_amount_f) 

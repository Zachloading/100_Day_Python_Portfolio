#This Project tells you how long you have to live assuming you live to 90 years of age. 
age = input("What is your current age? ")






months = 12
age_n = int(age)

result = 90 - age_n
result = result * 365
final_day = result 


result = 90 - age_n
result = result * 52
final_week = result 

result = 90 - age_n
result = result * 12
final_month = result 

str(final_day)
str(final_week)
str(final_month)

print (f"You have {final_day} days , {final_week} weeks, and {final_month} months left. ")
      
   

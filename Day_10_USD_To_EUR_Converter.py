'''
2/16/25
Zakareeya Amra
Goal: 
Create a script that converts USD to Euro
If the amount is less then 1 add an error message
Tell the user what to type
Stop the program if the value entered is less then 1
'''



#intro
print("Welcome to Zakareeya Amra's USD to EUR Converter. Currentely 1 USD is worth 0.9533 EUR according to Wise.com")


#var
USD = eval(input("Enter Value $: "))
EUR = USD * 0.9533

#function
if USD < 1:
    print("Error Value must be bigger then $1")
else:
    print("The conversion is complete. The total amount you have in EUR is:", "%.2f"% EUR, "EUR")
    print("Have a nice day!")
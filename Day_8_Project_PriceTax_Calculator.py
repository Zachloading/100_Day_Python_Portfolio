'''
2/6/25 Lab 1
By: Zakareeya Amra
Goal of the lab is to get the 
total of 3 items.
Total and tax should be printed sep.
'''
print("Please enter three item prices")
Item1 = eval(input("What is the price of Item 1 :$ "))
Item2 = eval(input( "What is the price of Item 2 :$ "))
Item3 = eval(input("What is the price of Item 3 :$ "))

TotalPrice = Item1 + Item2 + Item3 
print("Your total price is", "$", "%.3f"% TotalPrice)

Tax = TotalPrice * 0.06
print("Tax", "$", "%.3f"% Tax)

TotalPriceWithTax = TotalPrice + Tax
print("Total", "$", "%.3f"% TotalPriceWithTax)
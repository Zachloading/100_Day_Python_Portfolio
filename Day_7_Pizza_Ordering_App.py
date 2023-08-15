# 🚨 Don't change the code below 👇



print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
PizzaCost = 0

if size == str("S"):
  PizzaCost = 15
  
if size == str("M"):
  PizzaCost = 20 
  
if size == str("L"):
  PizzaCost = 25
 

if add_pepperoni == str("Y") and size == str("S"):
  PizzaCost = PizzaCost + 2 
elif add_pepperoni == str("N"):
  PizzaCost = PizzaCost + 0
else:
  PizzaCost = PizzaCost + 3
  

if extra_cheese == str("Y"):
  PizzaCost = PizzaCost + 1
  print("Your final bill is:" + " " + "$" + f"{PizzaCost}.")
else:
  PizzaCost = PizzaCost + 0
  print("Your final bill is:" + " " + "$" + f"{PizzaCost}.")

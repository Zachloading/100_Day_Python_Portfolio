"""
2/22/25
Zakareeya Amra
Goal:
Create a program that asks user to enter the weight of a package.
Based off the weight let the program output the rater per pound.
Must show the company name.
"""

print("Welcome to Amra's Speedy Shipping Company. Our rates are based on the weight of your item. Enter the weights of your items below to see the prices.")
print("Type 'done' when you have finished entering package weights.")

# Initialize variables
total_charges = 0

while True:
    # Input
    user_input = input("Enter the weight of your package (or type 'done' to finish): ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'done':
        break

    # Convert input to a float and ensure it's valid
    try:
        pounds = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue
    
    # Determine Rate Per Pound (RPP)
    if pounds <= 2:
        rpp = 1.10
    elif pounds > 2 and pounds <= 6:
        rpp = 2.20
    elif pounds > 6 and pounds <= 10:
        rpp = 3.70
    else:
        rpp = 3.80
    
    # Calculate Total Charge for the current package
    total_charge = pounds * rpp
    total_charges += total_charge

    # Output charge for the current package
    print(f"The RPP for this package is: ${rpp:.2f}")
    print(f"The Total Charge for this package is: ${total_charge:.2f}")

# Output total charges for all packages
print("\nThank you for using Amra's Speedy Shipping Company!")
print(f"The Total Charges for all packages is: ${total_charges:.2f}")

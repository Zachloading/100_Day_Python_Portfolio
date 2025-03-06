#Input the speed of the vehicle
speed = float(input("Enter the speed of the vehicle in miles per hour: "))

#Input the hours that were traveled
hours = int(input("Enter the number of hours the vehicle has traveled: "))

#Create the loop
print("Distance traveled for each hour:")
for hour in range(1, hours + 1):
    distance = speed * hour
    print(f"Hour {hour}: {distance} miles")

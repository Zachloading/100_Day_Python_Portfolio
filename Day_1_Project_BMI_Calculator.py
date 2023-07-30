height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")



height_N = float(height)
weight_N = int(weight)

BMI_ANSWER = int(weight_N / height_N ** 2)
print(str(BMI_ANSWER))



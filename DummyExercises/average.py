num1 = input("Enter first number:")
num2 = input("Enter second number:")
num3 = input("Enter third number:")

num1,num2,num3 = input("Enter three numbers(comma separated): ").split(",")
print(f"average is { (int(num1) + int (num2) + int (num3)) / 3}")




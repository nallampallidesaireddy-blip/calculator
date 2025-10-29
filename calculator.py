print("Select Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

# Taking user inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid input! Please choose a valid option.")

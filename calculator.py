num1 = int(input("Write a number here - "))
num2 = int(input("Write another number here - "))
operation = input("Write the operation which you want to run - \n")
if operation == "addition":
    print("The answer is - ", num1 + num2)
elif operation == "subtraction":
    print("The answer is - ", num1 - num2)
elif operation == "multiplication":
    print("The answer is - ", num1 * num2)
elif operation == "division":
    print("The answer is - ", int(num1 / num2))

print("Thanks for using our calculator. :D")

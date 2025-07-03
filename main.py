
#First ask the user to enter his name and then greet the user with a welcome message.
name = input("Enter your name: ")
print("Welcome to the Calculator, " + name) 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Ask the user for which operation they want to perform
print("Choose the operation you want to perform:")
print("1: Addition")
print("2: Substraction")
print("3: Multiplication")
print("4: Division")
number = input("Enter the number of the chosen operation: ")
if number == "1":
    print("Result:", num1 + num2)
elif number == "2":
    print("Result:", num1 - num2)      
elif number == "3":
    print("Result:", num1 * num2)
elif number == "4":
    print("Result:", num1 / num2)
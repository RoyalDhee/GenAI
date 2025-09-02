#Creating a calculator app

# Function to Add numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract (a, b):
    return a - b

# Function to multiply numbers
def multiply (a, b):
    return a * b

#Function to divide first number by second number
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# #function to perform swuare root
# def sqrs(a, b):


print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
# print("5. Divide")
# print("6. Divide")

# Take input of choice from user 
choice = input("Enter choice 1/2/3/4: ")

# Input of users
num1 = float(input("Input the first number: "))
num2 = float(input ("Input the second number: "))

# Perform task based on user input
if choice == '1':
    print("Result:", add(num1, num2 ))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid Choice")








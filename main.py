greeting = "Hello World"
my_name = "Matt"

print(greeting)
print("My name is " + my_name)
your_name = str(input("What is your name? "))
print("Hi " + your_name)

if your_name == "Adam":
    print("Your ID number is 001")
elif your_name == "Eve":
    print("Your ID number is 002")
else:
    print("You have no valid ID")

print("Let's do a simple multiplication")
num1 = float(input("Enter a number: "))
num2 = float(input("Now enter a second number: :"))
sum = str(num1 * num2)
print("The answer is " + sum)
print("Thank you " + your_name)
#Py Calculator

#Fn to add two numbers
def add(x, y):
	return x+y

#Fn to subtract two numbers
def subtract(x, y):
	return x-y

#Fn to multiplies two numbers
def multiply(x, y):
	return x*y

print("Select operation.")
print("1.Add")
print("2.Subract")
print("3.Multiply")

while True:
	#user input
	choice = input("Enter choice(1/2/3): ")

	#check the input
	if choice in ('1', '2', '3'):
		num1 = int(input("Enter first positive number: "))
		num2 = int(input("Enter second positive number: "))

		if choice == '1':
			print(num1, "+", num2, "=", add(num1, num2))

		elif choice == '2':
			print(num1, "-", num2, "=", subtract(num1, num2))

		elif choice == '3':
			print(num1, "x", num2, "=", multiply(num1, num2))

		#check if wants another operation or else break the while loop
		next_calculation = input("Wanna to another calculation? ([Y]es/[N]o): ")
		if next_calculation == "N":
			break

	else:
		print("Invalid Input")

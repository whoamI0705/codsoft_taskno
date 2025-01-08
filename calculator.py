#takes input from the user
num1 = float(input("Enter the first number:  "))
num2 = float(input("Enter the second number:  "))
#takes options as an integer value for arithmetic operations
print("Choose the desired arithmetic operation:\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division")
option = int(input("Enter either 1,2,3 or 4 based on the operations you choose from the above given options\n"))
#using dictionary to refer each options(integer value) as keys and their values as symbols for respective arithmetic operation
operation = {
    1:"+",
    2:"-",
    3:"*",
    4:"/"
}
#checking if the option falls or user input wrong option
if option in operation:
    #using eval() function for arithmetic operation
    result = eval(f"{num1} {operation[option]} {num2}")
    print(f"Final Output:- \n{num1} {operation[option]} {num2} = {round(result,2)}")
else:
    print("Please enter either 1,2,3 or 4!!")
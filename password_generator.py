# Program that generates a password for the user.
import random


print("Welcome to the password generator! We are here to generate a strong password as per your interest.")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#takes input from the user
total_letters = int(input("What number of letters would you like to have in your password?\n"))
total_numbers = int(input("What about numbers? How many would you like to have in your password?\n"))
total_symbols = int(input("Enter the number of symbols you would like to have:\n"))
#creating an empty list to append random letters,numbers and symbols
password = []
for i in range(total_letters):
    password += random.choice(letters)
for i in range(total_numbers):
    password += random.choice(numbers)
for i in range(total_symbols):
    password += random.choice(symbols)
#shuffle() method only works for list 
random.shuffle(password)
#concatinating the strings in the list.
password = "".join(password)
print(f"Here is your password: {password}")

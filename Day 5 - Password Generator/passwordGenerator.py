import string
import random

alphabets = list(string.ascii_lowercase) + list(string.ascii_uppercase)
symbol = list(string.punctuation)
digits = list(string.digits)

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password? \n"))
symbols = int(input("How many symbols would you like? \n"))
numbers = int(input("How many numbers would you like? \n"))
password = ''

for i in range(letters):
    password += alphabets[random.randint(0, len(alphabets) - 1)]

for i in range(symbols):
    password += symbol[random.randint(0, len(symbol) - 1)]

for i in range(numbers):
    password += digits[random.randint(0, len(digits) - 1)]

password = random.sample(password, len(password))
print(f"Here is your password: {''.join(password)}")

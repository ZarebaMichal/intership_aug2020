import random
import json
products = [
    {"name": "Prod1", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod2", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod3", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod4", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod5", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod6", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod7", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod8", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod9", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
    {"name": "Prod10", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
]
#obj_list = []


class ParentProduct:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name of this product is {self.name}")


# Task1
class Product(ParentProduct):
    """
    Child class of ParendProduct, takes name, amount and a price as arguments.
    """
    def __init__(self, name, amount, price):
        super().__init__(name)
        self.amount = amount
        self.price = price

    def show_price(self, currency):
        """
        Method for returning name and price of product with given currency.
        """
        print(f"{self.name} price is {self.price} {currency}")

    def show_amount(self):
        """
        Method for showing amount of a product.
        """
        print(f"{self.name} amount is {self.amount}")

    def calculate_total_value(self):
        """
        Method for calculating total value of a product.
        """
        return self.amount * self.price


# Generating random amount and price using random, in range of min and max of the product
for item in products:
    item['amount'] = random.randint(item['amount']['min'], item['amount']['max'])
    item['price'] = random.randint(item['price']['min'], item['price']['max'])

# Creating a list with Product Class objects
obj_list = [Product(item['name'], item['amount'], item['price']) for item in products]

# Creating dict with summary values and appending it to list.
sum_values = []
for item in products:
    temp_dict = {"name": item['name'], "summary_value": item['price'] * item['amount']}
    sum_values.append(temp_dict)

# Writing summary values, products and instances of Product class in json format.
with open('results_01.txt', 'w') as f:
    for dict in sum_values:
        json.dump(dict, f, indent=2)
        f.write('\n')
    for dict in products:
        json.dump(dict, f, indent=2)
    for obj in obj_list:
        json.dump(obj.__dict__, f, indent=2)

# Task2! Opis byl troche nie jasny, dlatego zrobilem dwa podejscia do zadania drugiego
# Ten ktory nie jest zakomentowany, uwazam za rozwiazanie
# W zakomentowanym zalozylem, ze uzytkownik musi podac dwie liczby
# while True:
#     try:
#         input_value = []
#         number = input("Input number in range (0-150) - (75-200): ")
#         # Slicing string to get integers and appending them to input_value list
#         for digit in number.split():
#             if digit.isdigit():
#                 input_value.append(int(digit))
#         # Checking if user provided 2 numbers
#         if len(input_value) < 2:
#             print('You need to provide 2 numbers')
#             continue
#         # Checking if first number is in MIN range
#         elif input_value[0] not in range(0, 151):
#             print('First number must be between 0-150')
#             continue
#         # Checking if second number is in MAX range
#         elif input_value[1] not in range(75, 201):
#             print('Second number must be between 75-200')
#             continue
#         # Checking if first number isn't greater than second one.
#         elif input_value[0] > input_value[1]:
#             raise ValueError
#
#     except ValueError:
#         print("First number should be greater than second one")
#     # If numbers are correct, print "Correct" and stop the loop.
#     else:
#         print("Correct!")
#         break


# Task2 Tutaj mozna podejsc do rozwiazania na dwa sposoby. Liczby zakresu moga byc generowane na nowo za kazdym razem,
# gdy uzytkownik poda zly numer, lub na sztywno przed petla while. Nie zostalo to sprecyzowane w tresci zadania.

# Create two random values in given range using random
min = 1
max = 0
while min > max:
    min = random.randint(0, 150)
    max = random.randint(75, 200)

while True:
    try:
        # Save input to input_value and provide user with range
        input_value = int(input(f"Input number in range {min} - {max}: "))
        # Check if input value is in given range, if not raise value error
        if input_value < min or input_value > max:
            raise ValueError
        else:
            print('Correct!')
            break
    except ValueError:
        print("Given number isn't in provided range")
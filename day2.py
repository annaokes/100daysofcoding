print("Welcome to the tip calculator!")

# Ask user what the total bill was

total_bill = input("What was the bill total?: £")
total_bill = float(total_bill)

percentage_to_pay = input("What percentage tip would you like to give? 10, 12 or 15?: ")
percentage_to_pay = int(percentage_to_pay)
percentage_to_pay = percentage_to_pay/100

people_to_split = input("How many people to split the bill?: ")
people_to_split = int(people_to_split)

total_per_person = round(((total_bill*percentage_to_pay)+total_bill)/people_to_split,2)

print(f'Each person should pay: £{total_per_person}')
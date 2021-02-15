#Coffee Machine Project

from art import day15


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(user_option):
    global continue_with
    if resources["water"] >= MENU[user_choice]['ingredients']['water']:
        if resources["coffee"] >= MENU[user_choice]['ingredients']['coffee']:
            if resources["milk"] >= MENU[user_choice]['ingredients']['milk']:
                continue_with
            else:
                print("Sorry there is not enough milk")
                continue_with = False
        else:
            print("Sorry there is not enough coffee & milk")
            continue_with = False
    else:
        print("Sorry there is not enough water, milk or coffee")
        continue_with = False


money_in_bank = 0
sum_of_money = 0

def collect_money():
    global continue_with,sum_of_money
    if continue_with:
        print("Please Insert Coins: ")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        sum_of_money = round((quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01),2)
        print(f'Here is how much you paid ${sum_of_money}')


def check_money(choice,coins):
    global continue_with, money_in_bank
    if continue_with:
        if MENU[choice]["cost"] > coins:
            print('sorry that is not enough money')
            continue_with = False
        if MENU[choice]["cost"] < coins:
            print(f"Here is your {choice} ☕, it cost ${MENU[choice]['cost']}, enjoy your brew! 😀 ")
            change = round(coins - (MENU[choice]['cost']),2)
            money_in_bank += round(coins-change,2)
            print(f'Here is your change: ${change}')
        if MENU[choice]["cost"] == coins:
            print(f"Here is your {choice} ☕, it cost ${MENU[choice]['cost']}, so there is no change, enjoy your brew! 😀")
            change = round(coins - (MENU[choice]['cost']),2)
            money_in_bank += round(coins-change,2)


def reduce_resources(user_option):
    global continue_with
    if continue_with:
        resources["water"] = resources["water"] - MENU[user_choice]['ingredients']['water']
        resources["coffee"] = resources["coffee"] - MENU[user_choice]['ingredients']['coffee']
        resources["milk"] = resources["milk"] - MENU[user_choice]['ingredients']['milk']


def report():
    print(f' Water: {resources["water"]}ml \n Milk: {resources["milk"]}ml \n Coffee: {resources["coffee"]}g \n Money: ${money_in_bank}')


continue_with = True
while continue_with:
    print(day15)
    user_choice = input("What would you like to drink? An Espresso, Latte or Cappuccino: \n").lower()
    if user_choice == 'report':
        report()
    elif user_choice == 'off':
        continue_with = False
    else:
        check_resources(user_option=user_choice)
        collect_money()
        check_money(choice=user_choice, coins=sum_of_money)
        reduce_resources(user_option=user_choice)


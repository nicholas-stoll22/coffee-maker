MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

def is_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry. There isn't enough {item} left.")
            return False
    return True

def coin_cointer():
    total = int(input("How many quarters do you have? ")) * 0.25
    total += int(input("How many dimess do you have? ")) * 0.1
    total += int(input("How many nickles do you have? ")) * 0.05
    total += int(input("How many pennies do you have? ")) * 0.01
    return total

def is_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Heres your change. Amount: ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry. You don't have enough money to make this purchase. Here's your refund.")
        return False

def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? We have espresso, latte, and cappuccino. If nothing sounds good, type 'off' to turn off the machine. Or tepe 'report' to see how many ingredients we have left. ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources(drink["ingredients"]):
            payment = coin_cointer()
            if is_transaction(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
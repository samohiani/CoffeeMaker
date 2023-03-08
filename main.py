def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")

def resource_sufficient(order_ingredient):
    """Returns True if order can be made, false if ingredients available are insufficient"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    total = 0.25 * int(input("how many quarters?: "))
    total += 0.1 * int(input("how many dimes?: "))
    total += 0.05 * int(input("how many nickles?: "))
    total += 0.01 * int(input("how many pennies?: "))
    return total

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources['money'] = 0
turn_off = False
while not turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Turning off...")
        turn_off = True
    elif choice == "report":
        report()
    elif choice in MENU:
        if resource_sufficient(MENU[choice]['ingredients']):
            pay = process_coins()
            if pay < MENU[choice]['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif pay > MENU[choice]['cost']:
                change = pay - MENU[choice]['cost']
                print(f"Here is ${round(change,2)} in change.")
                print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                print(f"Here is your {choice} ☕️. Enjoy!")
            resources['water'] -= MENU[choice]['ingredients']['water']
            if ("milk" in MENU[choice]['ingredients']):
                resources['milk'] -= MENU[choice]['ingredients']['milk']
            resources['coffee'] -= MENU[choice]['ingredients']['coffee']
            resources['money'] += MENU[choice]['cost']
    else:
        print("Put in a valid input!")

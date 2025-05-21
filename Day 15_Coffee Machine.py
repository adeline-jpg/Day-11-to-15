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
    "money": 0
}
def make_coffee(order, order_ingredient):
    for ingredients in order_ingredient:
        resources[ingredients] -= order_ingredient[ingredients]
    print(f"here's your {order}, enjoy!")
def resources_sufficient(order_ingredients):
    for ingredients in order_ingredients:
        if order_ingredients[ingredients] > resources[ingredients]:
            print("sorry there isn't enough ingredients!")
            return False
    return True
def process_coins():
    print("please insert coins.")
    quarters = int(input("how many quarters?: ")) *.25
    dimes = int(input("how many dimes?: ")) * .1
    nickles = int(input("How many nickles?: ")) *.05
    pennies = int(input("how manu pennies?: ")) * .01
    total = quarters + dimes + nickles + pennies
    return total
def transaction_successful(money_received, order):
    if money_received > MENU[order]["cost"]:
        change = round(money_received - MENU[order]["cost"], 2)
        print(f"Here is your change ${change}")
        resources["money"] += MENU[order]["cost"]
        return True
    if money_received < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False


ordering = True
while ordering:
    order = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        ordering = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        if resources_sufficient(MENU[order]["ingredients"]):
            total = process_coins()
            if transaction_successful(total, order):
                make_coffee(order,(MENU[order]["ingredients"]))



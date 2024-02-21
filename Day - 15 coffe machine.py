MENU = {
    "espresso": 
    {
        "ingredients": 
        {
            "water": 50,
            "milk":  0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": 
    {
        "ingredients": 
        {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    
    

    "cappuccino": 
    {
        "ingredients": 
        {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order):
    for item in resources:
        if order['ingredients'][item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    print("please insert coins")
    total  = int(input("how many Quarters: ")) * 0.25
    total += int(input("how many Dimes: ")) * 0.10
    total += int(input("how many Nickels: ")) * 0.05
    total += int(input("how many Pennies: ")) * 0.01
    return total
    
def is_transaction_successful(money_received , cost_drink):
    if money_received >= cost_drink:
        global profit
        change = round(money_received - cost_drink, 2)
        print (f"Here is ${change} in change")
        profit += cost_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name ,order_ingredients):
    for item in  order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Sorry, that's not a valid choice. Please try again.")

# Coffee machine
#  Three flavors - espresso, latte, cappuccino
#  Espresso - 50ml water, 18g coffee - $1.50
#  Latte - 200ml Water, 24g coffee, 150 ml milk - $2.50
#  Cappuccino - 250ml water, 24g coffee, 100 ml Milk - $3.00

# Coffee limits - 300ml water, 200ml milk, 100g coffee
# Coin operated - penny, nickel, dime, quarter
#
# Program requirements
#  1. Print report (resources - current water, milk, coffee, money amounts)  "report"
#  2. Check resources sufficient if user orders drink
#  3. Process coins for drinks.
#  4. Check that the transaction was successful.
#  5. Make Coffee and give change.

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
money = 0.00

# Print Resources in Coffee Machine
def print_resources():
    for k, v in resources.items():
        if k != "Coffee": # Measured in milliliters
            print(f"{k.title()}: {v}ml")      # Print the keys in Title case
        else:   # It's Coffee so we measure in grams
            print(f"{k.title()}: {v}g")
    print(f"Money: ${money:.2f}")       # Print two decimal places for the float

def take_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return(quarters, dimes, nickels, pennies)

def calculate_change(quarters, dimes, nickels, pennies):
    change = 0.00
    for coin in range(0,quarters):
        change += .25
    for coin in range(0,dimes):
        change += .10
    for coin in range(0,nickels):
        change += .05
    for coin in range(0,pennies):
        change += .01
    #print(change)
    return change

def compare_ingredients_to_resources(order):
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def make_drink(order):
    for item in order:
        resources[item] -= order[item]
        #print(resources[item])


def print_menu_with_costs():
    #print(f"Latte: {MENU['latte']['cost']:.2f}")        # Conversion of float to 2 decimal places is outside 'cost'
    for k, v in MENU.items():
        title = k.title()
        for key, value in v.items():
            if key == "cost":
                print(f"{title}: {value:.2f}")

def turn_off():
    print("Turning off machine.")
    quit()

machine_operable = True
while machine_operable is True:

    # Prompt user for input.
    selection = input("What would you like? (espresso/latte/cappuccino)")
    # print(f"selection was {selection}")

    # Do something based on selection
    if selection == "report":
        print_resources()
    elif selection == "off":
        turn_off()
    elif selection == "menu":
        print_menu_with_costs()
    else:
        order = MENU[selection]
        # Check if resources available to make selection
        if compare_ingredients_to_resources(order["ingredients"]) is True:
            # Prompt user to insert coins
            coins = take_coins()
            change = calculate_change(*coins)
            print(f"{change:.2f}")
            if change < order["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Making your drink: {selection} ☕")
                make_drink(order["ingredients"])
                money += change
                leftover_money = change - order["cost"]
                print(f"Your change is {leftover_money:.2f}")


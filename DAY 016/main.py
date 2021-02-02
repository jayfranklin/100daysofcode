from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create coffee maker,money machine, and menu
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Start the machine
is_operable = True

def turn_off():
    global is_operable
    is_operable = False
    quit()

while is_operable is True:
    selection = input(f"What would you like to order {menu.get_items()} ?").lower()
    if selection == "off":
        turn_off()
    elif selection == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(selection)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



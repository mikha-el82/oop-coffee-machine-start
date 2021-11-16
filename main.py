from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_menu = Menu()
machine = CoffeeMaker()
money_tray = MoneyMachine()
chosen_drink = ""
turning_off = False

while not chosen_drink and not turning_off:
    order = input(f"What would you like? ({machine_menu.get_items()}) ")
    if order == "report":
        machine.report()
        money_tray.report()
    elif order == "off":
        turning_off = True
    elif (chosen_drink := machine_menu.find_drink(order)):
        # chosen_drink = machine_menu.find_drink(order)
        if machine.is_resource_sufficient(chosen_drink) and money_tray.make_payment(chosen_drink.cost):
            machine.make_coffee(chosen_drink)
    chosen_drink = ""

if turning_off:
    print("Turning off!")
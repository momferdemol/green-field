from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while machine_is_on:

    choice = input(f"What would you like? {menu.get_items()}: ").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_is_on = False
        print("Machine shutdown")
    else:
        # get drink from menu
        drink = menu.find_drink(choice)
        # check resources sufficient and check transaction successful
        if (coffee_maker.is_resource_sufficient(drink)) and (money_machine.make_payment(drink.cost)):
            # make the drink from menu
            coffee_maker.make_coffee(drink)           
            
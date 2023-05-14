import src.data as data
import src.functions as function


def coffee_machine():

    balance = 0
    machine_is_on = True

    while machine_is_on:

        choice = function.get_user_choice()

        if choice == "report":
            function.get_machine_report(balance)

        elif choice == "off":
            machine_is_on = function.shutdown_machine()

        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            drink = data.MENU[choice]

            if function.is_resource_sufficient(drink["ingredients"]):
                payment = function.process_coins()

                if function.is_transaction_successful(payment, drink["cost"]):
                    balance = function.add_to_balance(balance, drink["cost"])
                    print(function.make_drink(choice, drink["ingredients"]))

        else:
            print("Error. Unknow command.")


coffee_machine()

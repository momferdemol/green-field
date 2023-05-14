import src.data as data


def get_user_choice():
    """Return string value from input function."""
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return choice


def get_machine_report(balance):
    """Print current state of machine resources."""
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Balance: ${balance}\n")


def shutdown_machine():
    """Return false to exit while statement."""
    print("Coffee machine is now shut down. 🧰\n") 
    return False   


def is_resource_sufficient(order_ingredients):
    """Return false when machine resources are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > data.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Ask for payment and return total value."""
    print("Please insert coins.")
    total = int(input("how may quarters?: ")) * 0.25
    total += int(input("how may dimes?: ")) * 0.1
    total += int(input("how may nickles?: ")) * 0.05
    total += int(input("how may pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return false when payment by user is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded. 👀")
        return False


def add_to_balance(balance, drink_cost):
    """Add payment to machine balance."""
    balance += drink_cost
    return balance


def make_drink(drink_name, order_ingredients):
    """Deduct drink ingredients from machine resources."""
    for item in order_ingredients:
        data.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

from art import logo

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

money = 0


def sufficient_resources(drink_type):
    """Check if the current resources are sufficient for the selected drink. Input the selected drink type."""

    is_sufficient = True
    for resource in MENU[drink_type]["ingredients"]:
        if not(MENU[drink_type]["ingredients"][resource] <= resources[resource]):
            print(f"Sorry there is not enough {resource}.")
            is_sufficient = False
    return is_sufficient


def transaction_successful(drink_type):
    """Check to see if the transaction was a success. Inputs are the coins the user gave."""
    total = 0
    cost = MENU[drink_type]["cost"]
    print(f"  A {drink_type} costs ${MENU[drink_type]['cost']}")
    total += float(input("      How many quarters? ")) * 0.25
    total += float(input("      How many dimes? ")) * 0.10
    total += float(input("      How many nickels? ")) * 0.05
    total += float(input("      How many pennies? ")) * 0.01

    if total >= cost:
        print(f"Here is ${total - cost} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def report():
    """Report the current resources in the coffee machine."""
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(money))


def make_coffee(drink_type):
    """Using the inputted drink type, reduce the corresponding resources values for that coffee."""
    for resource in MENU[drink_type]["ingredients"]:
        resources[resource] -= MENU[drink_type]["ingredients"][resource]
    print(f"Here is your {drink_type} ☕. Enjoy!")


def coffee_machine():
    """Main Code for the machine. Input the current money value."""
    # Option Menu, ask the user what they want
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # response to selected option
    if option == "report":
        report()

    elif option == "off":
        # Turn the machine off
        return

    elif option == "espresso" or option == "latte" or option == "cappuccino":
        if sufficient_resources(option):
            if transaction_successful(option):
                make_coffee(option)
    else:
        print(f"'{option}' is not a valid input.")

    coffee_machine()


# Execute the code and startup the coffee machine
print(logo)
coffee_machine()

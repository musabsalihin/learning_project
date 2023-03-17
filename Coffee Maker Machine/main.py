from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
#notEnoughMoney = False

options = menu.get_items()

while is_on is True:
    choice = input(f"What would you like? ({options}): ")
    
    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) is True:
            if money_machine.make_payment(drink.cost) is True:
                coffee_maker.make_coffee(drink)




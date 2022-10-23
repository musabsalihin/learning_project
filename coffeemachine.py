recipe = {
    'espresso':{
        'water': 50,
        'milk': 0,
        'coffee':18,
        'price':1,
    },
    'latte':{
        'water': 200,
        'milk': 150,
        'coffee':24,
        'price':2,
    },
    'cappucino':{
        'water': 250,
        'milk': 100,
        'coffee':24,
        'price':2.5,
    },
}

stock = {
    'water':300,
    'milk':300,
    'coffee':100,
    'money':0,
}

def process_drink(a):
    stock['coffee'] = stock['coffee'] - recipe[a]['coffee']
    stock['milk'] = stock['milk'] - recipe[a]['milk']
    stock['water'] = stock['water'] - recipe[a]['water']
    if stock['coffee']<0:
        print("Sorry there's not enough coffee.")
        return False
    elif stock['milk']<0:
        print("Sorry there's not enough milk.")
        return False
    elif stock['water']<0:
        print("Sorry there's not enough water.")
        return False
    else:
        return True
def add_stock():
    if stock['coffee']<=0:
        stock['coffee'] = int(input("Refill Coffee: "))
    elif stock['coffee'] > 0:
        stock['coffee'] += int(input("Add Coffee: "))

    if stock['water']<=0:
        stock['water'] = int(input("Refill water: "))
    elif stock['water']>0:
        stock['water'] += int(input("Add water: "))

    if stock['milk']<=0:
        stock['milk'] =int(input("Refill milk: "))
    elif stock['milk'] > 0:
        stock['milk'] += int(input("Add milk: "))
        
def payment(a):
    total_coin = 0
    quarter = int(input("How many quarters?: "))*0.25
    dime = int(input("How many dimes?: "))*0.1
    nickle = int(input("How many nickles?: "))*0.5
    penny = int(input("How many pennies?: "))*0.01
    total_coin = quarter+dime+nickle+penny
    if total_coin >= recipe[a]['price']:
        stock['money'] += recipe[a]['price']
        balance = round(total_coin - recipe[a]['price'],2)
        print(f"Here is ${balance} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def printReport():
    print(f"Coffee : {stock['coffee']}g")
    print(f"Water : {stock['water']}ml")
    print(f"Milk : {stock['milk']}ml")
def coffee_machine():
    machine_status = True
    while machine_status is True:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == 'report':
            printReport()
            stock['money'] = round(stock['money'],2)
            print(f"Money : ${stock['money']}")
        elif drink == 'off':
            machine_status = False
            break
        elif drink == 'add':
            add_stock()

        else:
            enough_resource = process_drink(drink)
            if enough_resource is True:
                completePayment = payment(drink)
                if completePayment is True:
                    printReport()
                    print(f"Here is your {drink}. Enjoy!")
            else:
                continue
    print("Machine is under maintenance.")

coffee_machine()
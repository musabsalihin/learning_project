def calculate(n1,n2, operator):
    if operator == '+':
        result = n1+n2

    elif operator == '-':
        result = n1-n2

    elif operator == '*':
        result = n1*n2

    elif operator == '/':
        while n1 == 0:
            print("First number can not be zero.")
            n1 = float(input("Please input first number: "))
        result = n1/n2

    return result


def save_history(num1, num2, operator, result):
    calchistory = {}
    calchistory["num1"] = num1
    calchistory["num2"] = num2
    calchistory["operator"] = operator
    calchistory["result"] = result
    history_list.append(calchistory)


def print_history(history):
    for n in range(history):
        print(f"{history_list[n]['num1']} {history_list[n]['operator']} {history_list[n]['num2']} = {history_list[n]['result']}")


def checkNext(next):
    if next == 'n':
        return True
    elif next == 'N':
        return True
    elif next == 'y':
        return True
    elif next == 'Y':
        return True
    else:
        return False

history_list = []

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

sen = 1
history = 0
next = 'n'
while sen > 0:
    if next == "n" or next == "N":
        n1 = float(input("Please input first number: "))
    else:
        n1 = result

    operator = input("Please choose your operation\n+\n-\n*\n/\n")
    while not (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
        print("Your operation is not valid\nPlease fill it again")
        operator = input("Please choose your operation\n+\n-\n*\n/\n")

    n2 = float(input("Please input second number: "))

    result = calculate(n1,n2,operator)

    history += 1
    save_history(n1, n2, operator, result)
    print(f"Result: {result}")

    next = input(f"If you wish to continue with previous value {result} press 'y'  if not press 'n'.\nIf you wish to terminate this program press any key.\n")
    if checkNext(next) is False:
        sen = -1

print("\n********************Calculation History*******************\n")
print_history(history)
print("\n-------------Thank you for using our service.-------------")

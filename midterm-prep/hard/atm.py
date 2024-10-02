# Create a program using dictionaries to simulate a simple bank account system. Each account has a name and balance. The user can deposit, withdraw, and check_balance.

# import libraries
import json
import os

# declare variables
data = {}
two_options = ["deposit", "withdraw"]
one_option = ["check"]
# DATA_FILE = "atm_data.json"
DATA_FILE = "test_atm_data.json"

# function for loading data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# function for saving data
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

data = load_data()

# function for depositing money
def deposit(name, value):
    try:
        value = float(value)
    except ValueError:
        return "Invalid deposit amount. Please enter a numeric value."

    if value < 0:
        return "Cannot deposit a negative amount."

    if name not in data:
        data[name] = value
        message = "account created and deposit successful"
    else:
        balance = data[name]
        data[name] = balance + value
        message = "deposit successful"
    save_data(data)
    return message

# function for withdrawing money
def withdraw(name, value):
    try:
        value = float(value)
    except ValueError:
        return "Invalid withdrawal amount. Please enter a numeric value."
    
    if value < 0:
        return "Cannot withdraw a negative amount."
    
    if name not in data:
        print("can't withdraw money because you don't have a registered account")
    else:
        balance = data[name]
        if value > balance:
            print("sorry, you don't have enough money to withdraw")
        else:
            data[name] = balance - value
            save_data(data)
            print("withdrawal successful")

# function for checking balance
def check(name):
    if name in data:
        balance = data[name]
        return f"your balance is {balance} dollars"
    else:
        return f"no account found for {name}, to create an account, deposit money"

# call functions
def callings(name, action, value):
    if action == "deposit":
        return deposit(name, value)
    elif action == "withdraw":
        return withdraw(name, value)
    else: # action can only be "check" a.k.a. action == "check"
        return check(name)

def do_the_rest(command):
            parts = command.split()
            if len(parts) == 3:
                name, action, value = parts

                if action not in two_options:
                    return "loop"
                try:
                    value = float(value)
                except ValueError:
                    return "loop"
            elif len(parts) == 2:
                name, action = parts
                value = None

                if action not in one_option:
                    return "loop"
            else:
                return "loop"
            if not name.isalpha():
                return "loop"
            return callings(name, action, value)

# main program
def main():
    print("Welcome to the ATM")
    print("You can deposit, withdraw, and check your balance")
    print("\nformat: name action value\n")
    print("EXAMPLE")
    print("deposit: john deposit 100")
    print("withdraw: john withdraw 50")
    print("check: john check")
    while True:
        command = input(": ")
        if command == "clear":
            os.system("clear")
        else:
            output = do_the_rest(command)
            if output == "loop":
                print("Invalid command. Please try again.")
                continue
            else:
                print(output)
        
# call main
if __name__ == "__main__":
    main()
# Create a program using dictionaries to simulate a simple bank account system. Each account has a name and balance. The user can deposit, withdraw, and check_balance.

# import libraries
import json
import os

# declare variables
data = {}
two_options = ["deposit", "withdraw"]
one_option = ["check"]
DATA_FILE = "atm_data.json"

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
    if name not in data:
        data[name] = float(value)
        print("account created and deposit successful")
    else:
        balance = data[name]
        data[name] = balance + value
        print("deposit successful")
    save_data(data)

# function for withdrawing money
def withdraw(name, value):
    if name not in data:
        print("can't withdraw money because you don't have a registered account")
    else:
        balance = data[name]
        if value > balance:
            print("sorry, you don't have enough money to withdraw")
        else:
            data[name] = balance - value
            print("withdrawal successful")
            save_data(data)

# function for checking balance
def check(name):
    # try:
    #     balance = data[name]
    #     return f"your balance is {balance} dollars"
    # except KeyError:
    #     return "you don't have an account with us, to create an account, deposit money"
    if name in data:
        balance = data[name]
        return f"your balance is {balance} dollars"
    else:
        return f"no account found for {name}"

# call functions
def callings(name, action, value):
    print("enter action checking")
    if action == "deposit":
        deposit(name, value)
    elif action == "withdraw":
        withdraw(name, value)
    elif action == "check":
        print(check(name))

def do_the_rest(command):
            try:
                name, action, value = command.split()
                print("pass split: split into 3 entities")
            except:
                print(f"fail split: result = FAIL TO SPLIT INTO 3 entities | input: {command}")
                print("proceeding with 2 entities split")
                try:
                    name, action = command.split()
                    print("pass split: split into 2 entities")
                except:
                    print(f"fail split: result = FAIL TO SPLIT INTO 2 entities | input: {command}")
                    return "loop"
            print("----------------------------------------------------")
            if len(command.split()) == 3:
                print("pass length check\t|\tlen = 3")
                if isinstance(name, str): # check whether it is str or not
                    print("pass name check\t\t|\tlen = 3")
                    if action in two_options:
                        print("pass action check\t|\tlen = 3")
                        try:
                            value = float(value)
                            print("pass value check\t|\tlen = 3")
                            callings(name, action, value)
                            # break
                        except ValueError:
                            print("fail value check\t|\tlen = 3")
                            return "loop"
                    else:
                        print("fail action check\t|\tlen = 3")
                        return "loop"
                else:
                    print("fail name check\t|\tlen = 3")
                    return "loop"
            elif len(command.split()) == 2:
                print("pass length check\t|\tlen = 2")
                if isinstance(name, str):
                    print("pass name check\t\t|\tlen = 2")
                    if action in one_option:
                        print("pass action check\t|\tlen = 2")
                        callings(name, action, None)
                        # break
                    else:
                        print("fail action check\t|\tlen = 2")
                        return "loop"
                else:
                    print("fail name check\t|\tlen = 2")
                    return "loop"
            else:
                print("fail length check\t|\tlen = 2")
                return "loop"

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
            print("\n" * 20)
            # os.system("clear")
        else:
            output = do_the_rest(command)
            if output == "loop":
                continue
            else:
                break
        
# call main
if __name__ == "__main__":
    main()
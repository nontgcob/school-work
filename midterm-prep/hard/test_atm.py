import json
import os
from atm import deposit, withdraw, check, callings, do_the_rest, DATA_FILE

# Fixture to reset the test data before each test
def reset_data():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as file:
        file.write('{}')

# Test Case 1: Test Deposit Function
def test_deposit():
    reset_data()
    # Test new account creation and deposit
    message = deposit("alice", 100)
    assert message == "account created and deposit successful", "Failed to create new account and deposit"
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        assert data["alice"] == 100.0, "Incorrect balance after deposit"

    # Test deposit into an existing account
    message = deposit("alice", 50)
    assert message == "deposit successful", "Failed to deposit into existing account"
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        assert data["alice"] == 150.0, "Incorrect balance after second deposit"

    # Test deposit with a non-numeric value
    message = deposit("alice", "fifty")
    assert message == "invalid deposit amount. Please enter a numeric value.", "Failed to handle non-numeric deposit"

    # Test depositing a negative amount
    message = deposit("alice", -50)
    assert message == "cannot deposit a negative amount.", "Failed to prevent depositing negative amount"

# Test Case 2: Test Withdraw Function
def test_withdraw():
    reset_data()
    # Setup an initial deposit
    deposit("bob", 200)

    # Test withdrawal with sufficient funds
    message = withdraw("bob", 50)
    assert message == "withdrawal successful.", "Failed to withdraw with sufficient funds"
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        assert data["bob"] == 150.0, "Incorrect balance after withdrawal"

    # Test withdrawal with insufficient funds
    message = withdraw("bob", 300)
    assert message == "sorry, you don't have enough money to withdraw.", "Failed to prevent withdrawal with insufficient funds"

    # Test withdrawal from a non-existent account
    message = withdraw("charlie", 50)
    assert message == "can't withdraw money because you don't have a registered account.", "Failed to prevent withdrawal from non-existent account"

    # Test withdrawal with a non-numeric value
    message = withdraw("bob", "fifty")
    assert message == "invalid withdrawal amount. Please enter a numeric value.", "Failed to handle non-numeric withdrawal"

    # Test withdrawing a negative amount
    message = withdraw("bob", -50)
    assert message == "cannot withdraw a negative amount.", "Failed to prevent withdrawing negative amount"

# Test Case 3: Test Check Balance Function
def test_check():
    reset_data()
    # Setup an initial deposit
    deposit("dave", 100)

    # Test checking balance for an existing account
    balance = check("dave")
    assert balance == "your balance is 100.0 dollars", "Failed to check balance for existing account"

    # Test checking balance for a non-existent account
    balance = check("eve")
    assert balance == "no account found for eve, to create an account, deposit money", "Failed to handle checking balance for non-existent account"

# Test Case 4: Test Callings Function (Deposit, Withdraw, Check)
def test_callings():
    reset_data()
    # Test deposit via callings
    message = callings("alice", "deposit", 50)
    assert message == "account created and deposit successful", "Failed deposit via callings"
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        assert data["alice"] == 50.0, "Incorrect balance after deposit via callings"

    # Test withdraw via callings
    deposit("alice", 100)  # Total should be 150
    message = callings("alice", "withdraw", 100)
    assert message == "withdrawal successful.", "Failed withdrawal via callings"
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        assert data["alice"] == 50.0, "Incorrect balance after withdrawal via callings"

    # Test check balance via callings
    balance_message = callings("alice", "check", None)
    assert balance_message == "your balance is 50.0 dollars", "Failed to check balance via callings"

# Test Case 5: Test Do The Rest Function (Command Parsing)
def test_do_the_rest():
    reset_data()
    # Test valid deposit command with 3 entities
    message = do_the_rest("bob deposit 100")
    assert message == "account created and deposit successful", "Failed to process valid deposit command"

    # Test valid withdrawal command with 3 entities
    message = do_the_rest("bob withdraw 50")
    assert message == "withdrawal successful.", "Failed to process valid withdrawal command"

    # Test valid check balance command with 2 entities
    message = do_the_rest("bob check")
    assert message == "your balance is 50.0 dollars", "Failed to process valid check balance command"

    # Test invalid command (missing value for deposit)
    message = do_the_rest("bob deposit")
    assert message == "loop", "Failed to handle invalid deposit command (missing value)"

    # Test invalid command (invalid action)
    message = do_the_rest("bob fly 100")
    assert message == "loop", "Failed to handle invalid action"

    # Test invalid command (invalid name format)
    message = do_the_rest("123 deposit 100")
    assert message == "loop", "Failed to handle invalid name format"

# Test Case 6: Edge Cases
def test_edge_cases():
    reset_data()
    # Test depositing zero amount
    message = deposit("frank", 0)
    assert message == "account created and deposit successful", "Failed to handle depositing zero amount"
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        assert data["frank"] == 0.0, "Incorrect balance after depositing zero"

    # Test withdrawing zero amount
    message = withdraw("frank", 0)
    assert message == "withdrawal successful.", "Failed to handle withdrawing zero amount"
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        assert data["frank"] == 0.0, "Incorrect balance after withdrawing zero"

# Test Case 7: Test Sequential Operations
def test_sequential_operations():
    reset_data()
    # Deposit, withdraw, and check balance in sequence
    deposit("george", 500)
    withdraw("george", 200)
    balance = check("george")
    assert balance == "your balance is 300.0 dollars", "Incorrect balance after sequential operations"

# Fancy print for test success
def test_success_message():
    print("\033[1;36m" + "*"*50)
    print("\033[1;32m  All tests passed successfully! Great job!  ")
    print("\033[1;36m" + "*"*50 + "\033[0m")

# Running all the test cases
if __name__ == "__main__":
    test_deposit()
    test_withdraw()
    test_check()
    test_callings()
    test_do_the_rest()
    test_edge_cases()
    test_sequential_operations()
    test_success_message()
import json
from atm import deposit, withdraw, check, callings, do_the_rest

# Test Case 1: Test Deposit Function
def test_deposit():
    # Test new account creation and deposit
    deposit("alice", 100)
    with open("test_atm_data.json", 'r') as file:
        data = json.load(file)
        assert data["alice"] == 100.0, "AssertionError: Failed to create new account and deposit the correct amount"

    # Test deposit into an existing account
    deposit("alice", 50)
    with open("test_atm_data.json", 'r') as file:
        data = json.load(file)
        assert data["alice"] == 150.0, "Failed to deposit the correct amount into an existing account"

    # Test deposit with a non-numeric value (should raise an error)
    try:
        deposit("alice", "fifty")
    except ValueError:
        pass
    else:
        assert False, "Failed to raise error on non-numeric deposit"

# Test Case 2: Test Withdraw Function
def test_withdraw():
    # Setup an initial deposit
    deposit("bob", 200)

    # Test withdrawal with sufficient funds
    withdraw("bob", 50)
    with open("test_atm_data.json", 'r') as file:
        data = json.load(file)
        assert data["bob"] == 150.0, "Failed to withdraw the correct amount with sufficient funds"

    # Test withdrawal with insufficient funds
    result = withdraw("bob", 300)
    assert result == "sorry, you don't have enough money to withdraw", "Failed to prevent withdrawal with insufficient funds"

    # Test withdrawal from a non-existent account
    result = withdraw("charlie", 50)
    assert result == "can't withdraw money because you don't have a registered account", "Failed to prevent withdrawal from a non-existent account"

    # Test withdrawal with a non-numeric value (should raise an error)
    try:
        withdraw("bob", "fifty")
    except ValueError:
        pass
    else:
        assert False, "Failed to raise error on non-numeric withdrawal"

# Test Case 3: Test Check Balance Function
def test_check():
    # Setup an initial deposit
    deposit("dave", 100)

    # Test checking balance for an existing account
    assert check("dave") == "your balance is 100.0 dollars", "Failed to check balance for an existing account"

    # Test checking balance for a non-existent account
    assert check("eve") == "no account found for eve", "Failed to handle checking balance for a non-existent account"

# Test Case 4: Test Callings Function (Deposit, Withdraw, Check)
def test_callings():
    # Test deposit via callings
    callings("alice", "deposit", 50)
    with open("test_atm_data.json", 'r') as file:
        data = json.load(file)
        assert data["alice"] == 200.0, "Failed deposit via callings"

    # Test withdraw via callings
    callings("alice", "withdraw", 100)
    with open("test_atm_data.json", 'r') as file:
        data = json.load(file)
        assert data["alice"] == 100.0, "Failed withdrawal via callings"

    # Test check balance via callings
    assert callings("alice", "check", None) is None, "Failed to check balance via callings"

# Test Case 5: Test Do The Rest Function (Command Parsing)
def test_do_the_rest():
    # Test valid deposit command with 3 entities
    result = do_the_rest("bob deposit 100")
    assert result is None, "Failed to process valid deposit command"

    # Test valid withdrawal command with 3 entities
    result = do_the_rest("bob withdraw 50")
    assert result is None, "Failed to process valid withdrawal command"

    # Test valid check balance command with 2 entities
    result = do_the_rest("bob check")
    assert result is None, "Failed to process valid check balance command"

    # Test invalid command (missing value for deposit)
    result = do_the_rest("bob deposit")
    assert result == "loop", "Failed to handle invalid deposit command (missing value)"

    # Test invalid command (invalid action)
    result = do_the_rest("bob fly 100")
    assert result == "loop", "Failed to handle invalid action"

    # Test invalid command (invalid name format)
    result = do_the_rest("123 deposit 100")
    assert result == "loop", "Failed to handle invalid name format"

# Test Case 6: Edge Cases
def test_edge_cases():
    # Test depositing zero amount
    deposit("frank", 0)
    with open("test_atm_data.json", 'r') as file:
        data = json.load(file)
        assert data["frank"] == 0.0, "Failed to handle depositing zero amount"

    # Test depositing a negative amount (shouldn't be allowed)
    try:
        deposit("frank", -100)
    except ValueError:
        pass
    else:
        assert False, "Failed to prevent depositing a negative amount"

    # Test withdrawing zero amount
    withdraw("frank", 0)
    with open("test_atm_data.json", 'r') as file:
        data = json.load(file)
        assert data["frank"] == 0.0, "Failed to handle withdrawing zero amount"

    # Test withdrawing a negative amount (shouldn't be allowed)
    try:
        withdraw("frank", -50)
    except ValueError:
        pass
    else:
        assert False, "Failed to prevent withdrawing a negative amount"

# Test Case 7: Test Sequential Operations
def test_sequential_operations():
    # Deposit, withdraw, and check balance in sequence
    deposit("george", 500)
    withdraw("george", 200)
    balance = check("george")
    assert balance == "your balance is 300.0 dollars", "Failed to maintain correct balance after sequential operations"

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

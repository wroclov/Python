import pytest
from bank_account import BankAccount, InsufficientFundsError

@pytest.fixture
def default_account():
    return BankAccount("Bob", 100)

def test_initial_balance(default_account):
    assert default_account.get_balance() == 100

@pytest.mark.parametrize("amount, expected", [
    (0, 100),
    (0.01, 100.01),
    (70, 170),
    (999_999_999_999, 1_000_000_000_099),
])
def test_deposit(default_account, amount, expected):
    default_account.deposit(amount)
    assert default_account.get_balance() == expected

@pytest.mark.parametrize("amount, expected_balance", [
    (0.01, 99.99),
    (40, 60),
    (100, 0),
])
def test_valid_withdrawals(default_account, amount, expected_balance):
    default_account.withdraw(amount)
    assert default_account.get_balance() == expected_balance

@pytest.mark.parametrize("invalid_amount, expected_exception", [
    (-1, ValueError),
    (0, ValueError),
    (101, InsufficientFundsError),
])
def test_invalid_withdrawals(default_account, invalid_amount, expected_exception):
    with pytest.raises(expected_exception):
        default_account.withdraw(invalid_amount)

def test_negative_deposit(default_account):
    with pytest.raises(ValueError):
        default_account.deposit(-77)

@pytest.mark.parametrize("amount, expected", [
    (0, 100),
    (0.01, 100.01),
    (60, 160),
    (9999, 10099),
])
def test_multiple_deposits(amount, expected):
    account = BankAccount("John", 100)
    account.deposit(amount)
    assert account.get_balance() == expected

@pytest.fixture
def alice_account():
    return BankAccount("Alice", 200)

@pytest.fixture
def mark_account():
    return BankAccount("Mark", 100)

def test_transfer_money(alice_account, mark_account):
    alice_account.transfer_to(mark_account, 50)
    assert alice_account.get_balance() == 150
    assert alice_account.get_balance() == 150

def test_transfer_insufficient_funds(mark_account, alice_account):
    with pytest.raises(InsufficientFundsError):
        mark_account.transfer_to(alice_account, 200)

@pytest.mark.parametrize("invalid_amount", [-1, -20, 0])
def test_transfer_negative_amount(alice_account, mark_account, invalid_amount):
    with pytest.raises(ValueError):
        alice_account.transfer_to(mark_account, invalid_amount)

def test_multiple_account_balances(alice_account, mark_account):
    charlie_account = BankAccount("Charlie", 300)
    alice_account.transfer_to(mark_account, 50)
    mark_account.transfer_to(charlie_account, 75)
    assert alice_account.get_balance() == 150
    assert mark_account.get_balance() == 75
    assert charlie_account.get_balance() == 375

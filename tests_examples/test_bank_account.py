import pytest
from bank_account import BankAccount, InsufficientFundsError

@pytest.fixture
def default_account():
    return BankAccount("Bob", 100)

def test_initial_balance(default_account):
    assert default_account.get_balance() == 100

def test_deposit(default_account):
    default_account.deposit(70)
    assert default_account.get_balance() == 170

def test_withdraw(default_account):
    default_account.withdraw(40)
    assert default_account.get_balance() == 60

def test_withdraw_insufficient_funds(default_account):
    with pytest.raises(InsufficientFundsError):
        default_account.withdraw(300)
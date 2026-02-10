from models.account import Account
from services.transaction_services import deposit

def test_deposit_with_positive_amount():
    # Ska inte kunna sätta in negativa belopp

    # Arrange
    # Dessa värden kollar ni från databasen utanför deposit-funktionen
    account = Account()
    account.id = 1
    account.balance = 200

    # Act
    form_data = {"amount": 50} # fås från formuläret
    result = deposit(form_data, account)
    # Assert
    assert result.balance == 200 + 50

def test_deposit_with_negative_amount():
    # Ska inte kunna sätta in negativa belopp

    # Arrange
    # Dessa värden kollar ni från databasen utanför deposit-funktionen
    account = Account()
    account.id = 1
    account.balance = 200

    # Act
    form_data = {"amount": -50} # fås från formuläret
    result = deposit(form_data, account)
    # Assert
    assert result.balance == 200

def test_deposit_with_missing_amount():
    # Ska inte kunna sätta in negativa belopp

    # Arrange
    # Dessa värden kollar ni från databasen utanför deposit-funktionen
    account = Account()
    account.id = 1
    account.balance = 200

    # Act
    form_data = {} # fås från formuläret
    result = deposit(form_data, account)
    # Assert
    assert result.balance == 200

def test_withdraw():
    # Ska inte kunna ta ut negativa belopp
    pass

def test_transaction():
    # Kombination av withdraw och deposit
    pass
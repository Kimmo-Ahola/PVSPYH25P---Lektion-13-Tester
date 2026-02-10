from models.account import Account

"""
# Kom ihåg att ni i riktiga bankappen har transaction kopplat
# till ett konto. Ni måste därför lägga till det i era tester.
def deposit(form_data: dict, account: Account):
    amount = form_data.get("amount")

    if amount is None or amount < 0:
        return False

    # Update balance
    account.Balance += amount

    # Create transaction
    transaction = Transaction(
        Type="DEPOSIT",
        Operation="Deposit",
        Date=datetime.now(),
        Amount=amount,
        NewBalance=account.Balance,
        AccountId=account.Id
    )

    return transaction
"""

def deposit(form_data: dict, account: Account):
    # Ska inte kunna sätta in negativa belopp
    try:
        amount = form_data["amount"]

        if amount < 0:
            return account
        
        account.balance += amount

        return account
    except:
        return account

def withdraw():
    
    pass

def transfer():
    pass
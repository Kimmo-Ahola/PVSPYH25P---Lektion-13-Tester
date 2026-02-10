from models.account import Account


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
# Constants for business rules
DAILY_LIMIT = 500.0
INITIAL_BALANCE = 1000.0

# State Management
balance = INITIAL_BALANCE
transaction_history = []
withdrawn_today = 0.0

def get_balance():
    return balance

def deposit(amount_str):
    global balance
    try:
        amount = float(amount_str)
        if amount <= 0:
            return False, "Error: Deposit must be a positive amount."
        
        balance += amount
        transaction_history.append(f"DEPOSIT: +${amount:,.2f}")
        return True, f"Success: ${amount:,.2f} deposited."
    except ValueError:
        return False, "Error: Invalid input. Please enter a numeric value."

def withdraw(amount_str):
    global balance, withdrawn_today
    try:
        amount = float(amount_str)
        
        if amount <= 0:
            return False, "Error: Withdrawal must be a positive amount."
        if amount > balance:
            return False, "Error: Insufficient funds."
        if (withdrawn_today + amount) > DAILY_LIMIT:
            remaining = DAILY_LIMIT - withdrawn_today
            return False, f"Error: Daily limit exceeded. You can only withdraw ${remaining:.2f} more today."
        
        balance -= amount
        withdrawn_today += amount
        transaction_history.append(f"WITHDRAW: -${amount:,.2f}")
        return True, f"Success: Please collect your ${amount:,.2f}."
    except ValueError:
        return False, "Error: Invalid input. Please enter a numeric value."

def get_statement():
    if not transaction_history:
        return ["No transactions recorded yet."]
    return transaction_history
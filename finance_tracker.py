from transaction import Transcation

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.balance = 0.0
    
    def add_transaction(self, amount, category, transaction_type):
        transaction = Transcation(amount, category, transaction_type)
        self.transactions.append(transaction)
        if transaction_type == 'income':
            self.balance += amount
        elif transaction_type == 'expense':
            self.balance -= amount
        print(f"Transaction added: {transaction_type} of {amount} for {category}")

    def view_transactions(self):
        print("\nTransaction History")
        for t in self.transactions:
            print(f"{t.date} - {t.transaction_type.capitalize()}: ${t.amount} | Category: {t.category}")
        print(f"\nCurrent Balance: ${self.balance:.2f}\n")
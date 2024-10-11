from transaction import Transcation
import json

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

    def save_transactions(self, filename):
        data = [{'amount': t.amount, 'category': t.category, 'transaction_type': t.transaction_type, 'date': t.date} for t in self.transactions]
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Transactions saved to {filename}")
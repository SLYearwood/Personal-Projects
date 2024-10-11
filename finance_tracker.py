from transaction import Transcation
import json

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.balance = 0.0
    
    def add_transaction(self, amount, category, transaction_type):
        if transaction_type == 'expense' and amount > self.balance:
            print("Not enough balance for this expense!")
            return
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

    def load_transactions(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.transactions = [Transaction(d['amount'], d['category'], d['transaction_type']) for d in data]
                self.balance = sum(t.amount if t.transaction_type == 'income' else -t.amount for t in self.transactions)
                print(f"Transactions loaded from {filename}")
        except FileNotFoundError:
            print(f"No file named {filename} found!")
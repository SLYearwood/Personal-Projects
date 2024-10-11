from finance_tracker import FinanceTracker

def main():
    tracker = FinanceTracker()
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            transaction_type = input("Enter 'income' or 'expense': ").lower()
            tracker.add_transaction(amount, category, transaction_type)
        elif choice == '2':
            tracker.view_transactions()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()

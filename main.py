from finance_tracker import FinanceTracker

# main.py (update the menu)

def main():
    tracker = FinanceTracker()
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Save Transactions")
        print("4. Load Transactions")
        print("5. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            transaction_type = input("Enter 'income' or 'expense': ").lower()
            tracker.add_transaction(amount, category, transaction_type)
        elif choice == '2':
            tracker.view_transactions()
        elif choice == '3':
            filename = input("Enter filename to save: ")
            tracker.save_transactions(filename)
        elif choice == '4':
            filename = input("Enter filename to load: ")
            tracker.load_transactions(filename)
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
from datetime import datetime

class Transcation: 
    def __init__(self, amount, category, transaction_type):
        self.amount - amount
        self.category = category
        self.transaction_type = transaction_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
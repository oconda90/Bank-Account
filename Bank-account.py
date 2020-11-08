class Account:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.Name = full_name
        self.AccountNumber = account_number
        self.Route = routing_number
        self.Balance = balance

    def deposit(self, amount):
        #deposit of money
        self.Balance = amount + self.Balance
        print(f'Amount Deposited = ${amount}')
    
    def Widthdrawl(self,amount):
        #The Overdraft fee
        if amount > self.Balance:
            self.Balance = self.Balance - amount
            print("Insufficient Funds")
            self.Balance = self.Balance - 10 
            print(f'Amount Withdrawn ${amount}')
        else:
            self.Balance =self.Balance - amount
            print(f'Amount Withdrawn ${amount}')
    
    def get_balance(self):
        print(f'Hey There, {self.Name}. Your account balance is ${round(self.Balance,2)} ')

    def add_interest(self):
        interest = self.Balance * 0.083
        self.Balance = self.Balance + interest
    
    def print_receipt(self):
        encrypt = '****'
        print(self.Name)
        print(f'Account No.: {encrypt + self.AccountNumber[4:9]}')
        print (f'Routing No.: {self.Route}')
        print(f'Balance: ${round(self.Balance,2)}')
class BankAccount:
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
        #getting personal balance :)
        print(f'Hey There, {self.Name}. Your account balance is ${round(self.Balance,2)} ')

    def add_interest(self):
        #adding interest :(
        interest = self.Balance * 0.083
        self.Balance = self.Balance + interest
    
    def print_receipt(self):
        #printing receipt at check-out
        encrypt = '****'
        print(self.Name)
        print(f'Account No.: {encrypt + self.AccountNumber[4:9]}')
        print (f'Routing No.: {self.Route}')
        print(f'Balance: ${round(self.Balance,2)}')

# 3 Personal acoount
OmarConda = BankAccount('Omar Conda','10606026', 32746927, 750.00)
CarlaLara = BankAccount('Carla Lara', '10211102', 78246723, 900.00)
TomuraShigaraki = BankAccount('Tomura Shigaraki', '56870349', 27834095, 50.00)

#making sure the code works :)
print('Hello to the terminal bank!')

print('   ')

OmarConda.get_balance()
OmarConda.deposit(30.50)
OmarConda.get_balance

print('   ')

CarlaLara.get_balance()
CarlaLara.Widthdrawl(20.75)
CarlaLara.get_balance

print('   ')

TomuraShigaraki.add_interest()
TomuraShigaraki.get_balance()

print('   ')

OmarConda.print_receipt()
CarlaLara.print_receipt()
TomuraShigaraki.print_receipt()
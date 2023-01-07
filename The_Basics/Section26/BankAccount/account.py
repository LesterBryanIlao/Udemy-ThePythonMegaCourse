
class Account:
    FILEPATH = "balance.txt"
    
    def __init__(self):
        with open(self.FILEPATH, 'r') as file:
            self.__balance = int(file.read())

    def __str__(self) -> str:
        return f"Your new balance is: {self.__balance}"

    def withdraw(self, amount):
        self.__balance -= amount
        self.commit()

    def deposit(self, amount):
        self.__balance += amount
        self.commit()
        
    def checkBalance(self):
        return self.__balance

    def commit(self):
        with open(self.FILEPATH, 'w') as file:
            file.write(str(self.__balance))



class Checking(Account):
    FILEPATH = "balance.txt"

    def __init__(self, fee):
        Account.__init__(self)
        self.fee = fee
        
    def transfer(self, amount):
        self.withdraw(amount+self.fee)
        
account = Account()


checking = Checking(15)
checking.transfer(170)
print(checking.checkBalance())

# account.withdraw(40)
# account.deposit(500)
# print(account.__str__())

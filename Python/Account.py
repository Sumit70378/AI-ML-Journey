class Account:
    Balance=0
    Account_Number=0
    def __init__(self,Balance,Account_Number):
        self.Balance = Balance
        self.Account_Number = Account_Number

    def debit(self,money):
        self.Balance=self.Balance-money

    def credit(self,money):
        self.Balance=self.Balance-money

    def printBal(self):
        print(self.Balance)

acc1 = Account(2000,12345)
acc1.debit(500)
acc1.printBal()
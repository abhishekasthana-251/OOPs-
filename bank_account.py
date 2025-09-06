class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initialAmount,accName):
        self.balance =initialAmount
        self.name=accName
        print(f"\nAccount '{self.name}' created.\nBalance = ₹{self.balance:.2f}")

    def getBalance(self):
         print(f"\nAccount '{self.name}'  Balance = ₹{self.balance:.2f}")


    def deposit(self,amount):
        self.balance=self.balance+ amount
        print("Deposit completed")
        self.getBalance()
    

    def viableTransaction(self,amount ):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has a balance of ₹{self.balance:.2f}"
            )
    

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance =self.balance-amount
            print("\n withdraw complete. see you next time THANK YOU")
            self.getBalance()

        except BalanceException as error:
            print(f'\n Withdraw interrupted : {error}')

    def transfer(self ,amount ,account):
        try:
            print ("\n ************ \n\n Beginning Transfer .. 🚀 .. .. .. .\n\n\n. .⌛")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n Transfer complete !   ✅  \n\n *******' )
        except BalanceException as error:
            print(f"\n Transfer interrupted . ❌⚔️☠️ {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance=self.balance+(amount*1.05)
        print("\n deposit complete. to the interestRewards Account ")
        self.getBalance()

class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee=5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance=self.balance -(amount + self.fee)
            print("\n Withdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted : {error}')
    

    
        
        
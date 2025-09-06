from bank_account import *

Abhishek =BankAccount(1000,"Abhishek")
Yash =BankAccount(2000,"Yash")


Abhishek.getBalance()
Yash.getBalance()

Yash.deposit(340.92)

Yash.withdraw(10.45)
Abhishek.transfer(300, Yash)

Aniket=SavingAcct(10203,'Aniket')

Aashish=InterestRewardsAcct(1032,'Aashish')

Aashish.transfer(200,Abhishek)

Aashish.getBalance()

Aniket.deposit(1023)

Aniket.transfer(2310,Yash)

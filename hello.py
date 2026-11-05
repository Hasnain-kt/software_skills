
class Bankaccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self , amount):
        self.balance = self.balance + amount
        

    def withdraw(self , amount):
        self.balance = self.balance - amount


payment = Bankaccount("hasnain" , 1000)
payment.deposit(500)
payment.withdraw(300)

print(payment.balance)








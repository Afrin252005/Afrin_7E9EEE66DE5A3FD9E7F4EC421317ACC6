class BankAccount:

 def                                 __init__(self, account_number, account_holder_name,initial_balance=0.0):
   self.__account_number=account_number
   self.__account_holder_name=account_holder_name
   self.__amount_balance=initial_balence
   def deposit(self,amount):
    if amount>0:
     self.__amount_balance+=amount
     print("deposited {}.New balance:{}".format(amount,self.__ amount_balance))
  else:
     print("Invalid deposit amount.please deposit positive")
  def withdraw(self, amount):
    if amount > 0 and               amount<=self.__amount_balance:
      self.__amount_balance -=amount
      print("withdraw {}.now balance:{}".format(amount,self.__amount_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance")
  def display_balance(self):
      print("Account balance for{}(Account#{}):{}". format (self.__account_holder_name,self.__account_number,self.__amount_balance))
        account=BankAccount(account _number="123456789",              
                            account _holder_name="Afrin Banu",
                            initial_balance=5000.0)
        account.display_balance()
        account.deposit(10000.0)
        account.withdraw(500.0)
        account.display_balance()
    
    
   
   
  
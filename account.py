class Account:
    def __init__(self,number,pin,interest_rate):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.interest_rate = interest_rate
        self.__frozen = False
        self.__transaction = []
        
    def show_balance(self, pin):
        if pin == self.__pin:
            return self.__balance   
    def deposit(self, money):
         self.__balance = self.__balance + money
         print(self.__balance)

    def withdraw(self,money):
        if self.__balance >= money:
         self.__balance = self.__balance - money
         print(self.__balance)
        else:
         print("There is insufficient amount in the account")
    def  view_account_details(self, name):
       print(f"{name} your acount number is {self.number} and your account balance is {self.__balance}") 
    def overdraft_limit(self, amount):
       if self.__balance < amount + 5:
          print("Insufficient funds would you like to apply for an overdraft.") 
       else:
          print(f"{self.__balance}")
    def apply_interest(self):
       interest_amount = self.show_balance()  *  self.interest_rate
       self.deposit(interest_amount) 
       print(f"Interest added {interest_amount} and the new balance is{self.show_balance()}.") 
    def freeze_account (self):
       self.__frozen = True
       print(self.__frozen)

    def transaction_history(self,deposit,withdraw):
       self.__transaction.append(deposit)
       self.__transaction.append(withdraw)
       print(self.__transaction)
    def set_minimum_balance(self,min_balance,pin):
       if pin == self.__pin:
         self.__minimum_balance == min_balance
         return f"Minimum balance requirement set to ${min_balance}"
       else:
          return "Wrong pin"
    def transfer_funds(self, amount,recipient_number,pin):
       if pin == self.__pin:
          if self.__balance >= amount:
             self.__balance -= amount
             self.__transaction.append(f"Withdrawal: ${amount} to {recipient_number}") 
             return f"Funds transferred successfully. New balance: ${self.__balance}"
          else:
             return "Insufficient funds."
       else:
          return "Wrong PIN"
    def close_account(self,pin):
       if pin == self.__pin:
          return "Account closed."
               






     





          

   

           

        

        
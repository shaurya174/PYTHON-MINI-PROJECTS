class Account:#Parent Class
    def __init__(self,fullName,account_number,account_password,balance):
        self.fullName = fullName
        self.account_number = account_number
        self.__account_password = account_password
        self.balance = balance
    def credit(self,credit_amount):
        self.credit_amount = credit_amount
        self.balance+=self.credit_amount
        print("Request Accepted....")
        self.print_balance()

    def debit(self,debit_amount):
        self.debit_amount = debit_amount
        self.balance-=self.debit_amount
        print("Request Accepted....")
        self.print_balance()
    def print_balance(self):
        print("Account Balance ->",self.balance)

class Bank(Account):#Child Class
    name = "ABC Bank"
    @staticmethod
    def print_bank():
        return Bank.name
    def greeting(self):
        print("Welcome To",Bank.print_bank())
        print("Hello,",self.fullName)

user_name = input("Enter Your Name: ")
user_account_number = int(input("Enter Your Account Number: "))
user_account_password = input("Enter Your Password: ")
user_balance = int(input("Enter Your Balance: "))
c1 = Bank(user_name,user_account_number,user_account_password,user_balance)
c1.greeting()
print("Our Bank Offers The Following Services (Enter The Number To Access A Service)")
print("1 -> print balance\n2 -> credit\n3 -> debit\n4 -> quit")
user_yes = True
while user_yes:
    user_choice = input("Your Choice -> ")
    if(user_choice=="2"):
     credit_amount = int(input("\nCredit Amount: "))
     print("\n")
     c1.credit(credit_amount)
    elif(user_choice=="3"):
     debit_amount = int(input("\nDebit Amount: "))
     print("\n")
     c1.debit(debit_amount)
    elif(user_choice=="1"):
     print("\n")
     c1.print_balance()
    elif(user_choice=="4"):
     print("Wish You A Good Day!")
     print("Closing Program.....")
     user_yes=False
     break
    else:
     print("ERROR....")
     print("Invalide Input!")
     user_yes=False
     break
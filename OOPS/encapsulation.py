# ENCAPSULATION = HIDING data from outside world
# Like a CAPSULE hides medicine inside it
# We use private variables (__ double underscore) to HIDE data
# We use getter & setter methods to ACCESS that hidden data

class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner          = owner       # public   (anyone can access)
        self.__balance      = balance     # private  (hidden! __ makes it private)
        self.__pin          = 1234        # private  (very secret!)
        self.__transactions = []          # private  (hidden transaction history)
    
    # ✅ GETTER method - to READ private data
    def get_balance(self):
        return self.__balance
    
    # ✅ SETTER method - to UPDATE private data (with validation)
    def deposit(self, amount):
        if amount > 0:                         # validation check
            self.__balance += amount
            self.__transactions.append(f"Deposited: +{amount}")
            print(f"✅ Deposited ₹{amount} successfully!")
        else:
            print("❌ Invalid amount! Amount must be greater than 0")
    
    def withdraw(self, amount, pin):
        if pin != self.__pin:                  # pin check
            print("❌ Wrong PIN! Access Denied!")
        elif amount > self.__balance:          # balance check
            print("❌ Insufficient Balance!")
        elif amount <= 0:
            print("❌ Invalid amount!")
        else:
            self.__balance -= amount
            self.__transactions.append(f"Withdrawn: -{amount}")
            print(f"✅ Withdrawn ₹{amount} successfully!")
    
    def show_transactions(self, pin):
        if pin == self.__pin:
            print("\n📋 Transaction History:")
            for t in self.__transactions:
                print(f"   {t}")
        else:
            print("❌ Wrong PIN! Cannot show transactions!")
    
    def show_account(self):
        print(f"Account Owner : {self.owner}")
        print(f"Balance       : ₹{self.__balance}")


# ✅ Using the BankAccount
print("======= Bank Account =======")
account = BankAccount("Rahul", 5000)

account.show_account()

print("\n--- Depositing Money ---")
account.deposit(2000)
account.deposit(-500)   # invalid

print("\n--- Withdrawing Money ---")
account.withdraw(1000, 1234)    # correct pin
account.withdraw(500,  9999)    # wrong pin
account.withdraw(99999, 1234)   # insufficient balance

print("\n--- Current Balance ---")
print(f"Balance: ₹{account.get_balance()}")

account.show_transactions(1234)

# ❌ Trying to access private variable directly - will give error
print("\n--- Trying to access private data directly ---")
try:
    print(account.__balance)   # This will FAIL!
except AttributeError:
    print("❌ Cannot access __balance directly! It is PRIVATE!")
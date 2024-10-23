

def reverse(s):
    s = s[::-1]
    return print(s)


class BankAccount:
    
    def __init__(self, balance = 0):
        self.balance = balance
        
        
       
        
        
    def withdraw(self,amount):
        
        self.balance -= amount
    
        
        print(f"You withdrew: ${amount}\nYour current balance is: ${self.balance}")
        
        
    
    def deposit(self,money_in):

        self.balance += money_in
        print(f"You deposited: ${money_in}\nYour current balance is: ${self.balance}")
            
    def total_balance(self):
        
        print(f"Your balance is: ${self.balance}")
        
        
def sort(nums):
    nums = []
    
    return nums.sorted()


def leap_year(year):
   
    
    if year % 4 and not year%400 or year%400:
        return "Leap year"
    
    return "Not a leap year"
    
    
        
        
        
    
        
        


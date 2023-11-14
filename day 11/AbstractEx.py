
from abc import ABC,abstractmethod
class Accounts:
    def savings(self):
        print("Savings account, no need of balance with 7% interest")

class Loans(ABC):

    @abstractmethod
    def pl(self):
        print("Personal loan")

    @abstractmethod #decorator
    def hl(self):
        print("Housing Loan")

#obj1 = Accounts()
#obj2 = Loans() #should not be created
#obj1.savings()
#obj2.pl() # should not be created

class FinalAccount (Accounts, Loans):
    def pl(self):
        print ("Persoanl Loan with 11% int")

    def hl (self):
        print("Home Loan with 8% Floating Int")

obj1 = FinalAccount()
obj1.savings()
obj1.pl()
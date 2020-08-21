class Account():
    """Represents a bank account."""

    def __init__(self, iD=0, balance=100, annualInterestRate=0):
        """Constructor creates an Account object with a default id value of 0, 
        a balance with a default value of 100, And the annual
        interest rate with a default value of 0"""
        
        self.__id = int(iD)
        self.__balance = float(balance)
        self.__annualInterestRate = float(annualInterestRate/100)
    
    
    def getId(self):
        """ Returns the account's ID number"""
        return self.__id

    
    def getMonthlyInterestRate(self):
        """Returns the monthly interest rate."""
        return (self.__annualInterestRate/12)*100

    
    def getMonthlyInterest(self):
        """Returns the monthly interest."""
        return  self.__balance * (self.__annualInterestRate/12)

    
    def getBalance(self):
        """Returns the account balance."""
        return self.__balance

    
    def setBalance(self,balance):
        """Sets the account balance."""
        self.__balance =  balance


    def setId(self,ID):
        """Sets the account number to the one entered within the parameter."""
        self.__id = ID


    def setAnnualInterestRate(self,AnnualInterest):
        """ Sets the Annual Interest rate to the one entered within the parameter."""
        self.__annualInterestRate = AnnualInterest

        
    def withdraw(self, amount):
        """reduces the account balance by amount."""
        self.__balance = self.__balance - amount

        
    def deposit(self, amount):
        """increases the account balance by amount."""
        self.__balance = self.__balance + amount

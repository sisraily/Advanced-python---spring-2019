"""
Name: Shimon Israily
Advanced python programming
This stock.py manages stock's symbol, name, previous and current prices.
"""

class Stock:
    """Represents a stock"""
    
    
    def __init__(self,symbol, name, previousClosingPrice, currentPrice):
        """Constructor creates an object of type Stock with a symbol, name, closing price, and current price"""
        self.__symbol = str(symbol)
        self.__name = str(name)
        self.__previousClosingPrice = float(previousClosingPrice)
        self.__currentPrice = float(currentPrice)
    
    def setCurrentPrice(self, currentPrice):
        """Sets the current stock price"""
        self.__currentPrice = currentPrice
    
    def setPreviousClosingPrice(self, previousClosingPrice):
        """Sets the previous closing stock price"""
        self.__currentPrice = currentPrice
    
    def getName(self):
        """Returns the stock name"""
        return self.__name
    
    def getSymbol(self):
        """Returns stock symbol"""
        return self.__symbol
    
    def getCurrentPrice(self):
        """returns the current stock price"""
        return self.__currentPrice
    
    def getPreviousPrice(self):
        """returns the previous stock price"""
        return self.__previousClosingPrice 
    
    def setCurrentPrice(self):
        """sets the current stock price"""
        return self.__currentPrice
    
    def setPreviousPrice(self):
        """sets the previous stock price"""
        return self.__previousClosingPrice  
    
    def getChangePercent(self):
        """returns the percent change between current and previous price"""
        return ((self.__currentPrice - self.__previousClosingPrice)/self.__previousClosingPrice)*100
    
    

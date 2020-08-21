from stock import Stock

def main():
    # construct an object of type Stock with a stock symbol, company name, previous price,
    # current price. The object is then to the variable stock1.
    stock1 = Stock("INTC", "Intel Corporation", 20.5, 20.35)
    
    # calls the get_change_percent method within stock1 object.
    # This method returns the percent change between the previous stock price and current stock price.
    print("{} price change of {:.2F}%".format(stock1.getName(),stock1.getChangePercent()))

# calls the main function.
main()

from account import Account

def main():
    # construct an object of a type account, with its attributes id to equal 1122, price at 20000,
    # interest rate at 4.5 percent annually.
    alex = Account(1122,20000,4.5)

    # Calls the withdraw method within the alex object with 2500 as aparameter.
    # This function subtracts 2500 from the balance attribute.
    alex.withdraw(2500)


    print("ID: {}\nBalance: ${}\nMonthly Interest Rate: {}%\nMonthly Interest: ${}".format(alex.getId(),
                                                                                    alex.getBalance(),
                                                                                    alex.getMonthlyInterestRate(),
                                                                                    alex.getMonthlyInterest()))


# calls the main function.
main()

Customers = []
Account_balance = 50.00
def bank():
    print("Welcome\n")
    access = input("To create an account, press 1\n" + "For Transaction, press 2\n")
    if access == "1":
        return Create_account()
    elif access == "2":
        return Transaction()
    else:
        print("Try Again!!!")

def Create_account():
    email = input("Enter email: ")
    password = input("Enter password: ")
    if (email and password != Customers):
        customer_email = Customers.insert(0, email)
        customer_password = Customers.insert(1, password)
        customer_balance = Customers.insert(2, Account_balance)
        print("Welcome, " + email)
        return Transaction()

def Transaction():
    print("Verify your account")
    password = input("Enter password: ")
    if password == Customers[1]:
        print("How can we help you?")
        options = input("Press 1: Check Balance\n" + "Press 2: Deposit\n" +
                        "Press 3: Withdrawal\n" + "Press 4: Transfer\n")
        if options == "1":
            return Check_balance()
        elif options == "2":
            return Deposit()
        elif options == "3":
            return Withdrawal()
        elif options == "4":
            return Transfer()
        else:
            print("Incorrect option")
    else:
        print("Unauthorized user")
        return Create_account()

    print(Customers)
    return Customers

def Check_balance():
    print("Your account balnce is £" + str(Customers[2]))
    return bank()

def Deposit():
    print("Please, make your deposit\n")
    amount = int(input("Enter amount to be deposited: \n"))
    new_balance = (int(Customers[2]) + amount)
    Customers[2] = new_balance
    print("Your account has been credited with £" + str(amount))
    print("Your account balance is £" + str(new_balance))
    return bank()

def Withdrawal():
    amount = int(input("Enter an amount to withdraw: \n"))
    if int(Customers[2]) == 0.00:
        print("Deposit money into your account")
        return Deposit()
    elif amount > int(Customers[2]):
        print("Insufficient balance")
        return Deposit()
    else:
        new_balance = int(Customers[2]) - amount
        Customers[2] = new_balance
        print("£" + str(amount) + " has been deducted from your account")
        print("Available balance: £" + str(new_balance))
        return bank()

def Transfer():
    print("Enter email of recipient")
    recipient = input("Enter email address: \n")
    amount = int(input("Enter amount to transfer: "))
    if amount > int(Customers[2]):
        print("Insufficient balance")
        return Deposit()
    else:
        new_balance = int(Customers[2]) - amount
        Customers[2] = new_balance
        print("£" + str(amount) + " has been transferred to " + recipient)
        print("Available balance: £" + str(new_balance))
        return bank()

bank()

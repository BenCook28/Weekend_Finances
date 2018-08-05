import pandas as pd, numpy as np

print("Please enter your last know account balance")
balance = input()
balance = int(balance)

print("What is your threshold")
threshold = input()
threshold = int(threshold)
            
while True:
    print("Please enter your transaction with an income as a negative number and an expense as a positive number")
    transaction = input()
    transaction = int(transaction)

    balance = balance - transaction

    print("Your account balance is now " + str(int(balance)) + ".")

    if balance <= threshold:
        print("Time to stop spending")

        print("Has your bank posted transactions yet")
        posted = input()
        posted = posted.upper()
        if posted == "YES":
            break
        else:
            continue

        print("Do you have any more transactions?")
        moreTransactions = input()
        moreTransactions = moreTransactions.upper()
        if moreTransactions == "YES":
            continue
        else:
            break
        
    

    

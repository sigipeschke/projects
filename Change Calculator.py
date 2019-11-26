"""
This program will process a monetary transaction between 0.01$ and 1000.00$ being payed in cash.

>Input from the console on how much cash is being used to pay for the merchandise.

>Calculates and outputs the total change for the transaction.
"""
import random
from time import perf_counter

def roundCashTotalDown(CashTotal):
    #round down to the nearest 0.5
    roundingDigit = int(str(CashTotal)[-1:])
    if roundingDigit >= 5:
        roundingDigit = 5
    else:
        roundingDigit = 0
    return float(str(CashTotal)[:-1] + str(roundingDigit))

def transactionCash(Total):
    #round total down to nearest 0.5
    Total = roundCashTotalDown(Total)
    
    #take input from the console for the cash amount being used to pay for the merchandise
    #Payment = input()
    Payment = 1100

    #process the amount of change due
    Change = round(float(Payment) - float(Total), ndigits = 2)

    #output the change due to the customer
    if Change >= 0:
        print('The amount of change is:', str(Change) + '$')
    #output an error if payment < total
    else:
        print('Error: Not a sufficient amount')
        print('The remaining amount necessary is:', str(Change)[1:] + '$')
        transactionChange(Total)

time_start = perf_counter()
for i in range(1000):
    #randomly generate a total for the monetary transaction to be between 0.01$ and 1000.00$
    Total = round(random.uniform(0.01, 1000.00), ndigits = 2)
    print('The total is:', str(Total) + '$')

    transactionCash(Total)

time_stop = perf_counter()

print("Elapsed time:", time_stop - time_start)

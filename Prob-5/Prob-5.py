# Module 2
#   Programming Assignment 3
#     Prob-5.py

# Riley Hewes

# You purchased the following:
#   - 2 slices of pizza at $2.00 per slice
#    - 1 large Coke at $1.50
#    - 2 donuts at $0.56 each
# print the items purchased and their cost, one item per line
# print the total of all items
# print the sales tax (8.4% of the total)
# print the grand total
# ask the user to enter an amount
# print the amount tendered
# print the change due

#Pizza @ 2:       4.0
#Drink:           1.5
#Donut @ 2:       1.12
#----------------------
#Subtotal:        6.62
#Tax:             0.56

#Total:           7.18

#Please enter an amount: 10
#Tendered:       10.00
#Change:         2.82

import math
def main():
    # items purchased
    Pizza = 2.00
    Coke = 1.50
    Donut = 0.56

    # other variables
    Subtotal = Pizza*2+Coke+Donut*2
    Tax = 0.56
    Total = Subtotal+Tax

    # receipt
    print("Items purchased:")
    print()
    print("Pizza x2:\t",Pizza*2)
    print("Coke:    \t",Coke)
    print("Donuts x2:\t",Donut*2)
    print()
    print("Subtotal:\t",Pizza*2+Coke+Donut*2)
    print("Tax:     \t",(Pizza*2+Coke+Donut*2)*.084)
    print()
    print("Total:   \t",Subtotal+Tax)
    print()
    Paid = int(input("Please enter an amount: "))
    print("Tendered:\t",Paid)
    print("Change:  \t",Paid-Total)

main()
# calculate florida sales tax for a given amount
def main():
    # get the amount of the purchase
    amount = float(input("Enter the amount of the purchase: "))
    # calculate the tax
    tax = amount * 0.07
    # display the result
    print("The tax is $", format(tax, ',.2f'), sep='')
    # print the total including tax
    print("The total is $", format(amount + tax, ',.2f'), sep='')

# run the main function
main()

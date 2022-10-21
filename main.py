# This program is an expense tracker.

# Import libraries
import numpy as np
import pandas as pd
from datetime import date

# Create empty lists
goods_Or_Services = []
prices = []
dates = []
expense_type = []

# Function to add expenses to the lists and organise data
def add_expense(goods_or_service, price, date, expense_Type):
    goods_Or_Services.append(goods_or_service)
    prices.append(price)
    dates.append(date)
    expense_type.append(expense_Type)

# Main
option = -1 # This is the user's option or choice or input.
while(option != 0):
    # Create the option menu
    print('Welcome to the expense tracker')
    print('1. Add food expense')
    print('2, Add household expense')
    print('3. Add transportation expense')
    print('4. Show and save the expense report')
    print('0. Exit')

    option = int(input('Choose an option: \n'))

    # Print new line for formatting
    print()
    # Check for the user's choice or option or input
    if option == 0:
        print('Program exit')
        break
    elif option == 1:
        print('Adding food')
        expense_Type = 'Food'
    elif option == 2:
        print('Adding household expense')
        expense_Type = 'household expense'
    elif option == 3:
        print('Adding transportation expense')
        expense_Type = 'transportation'
    elif option == 4:
        # Create a dataframe to add expenses
        expense_Report = pd.DataFrame()
        expense_Report['Goods or Services'] = goods_Or_Services
        expense_Report['Prices'] = prices
        expense_Report['Dates'] = dates
        expense_Report['Expense type'] = expense_type
        # Save expense report
        expense_Report.to_csv('expense.csv')
        # Show the expense report
        print(expense_Report)
    else:
        print('Error: You have chosen an incorrect option! Please try again. ')

# Allow the user to enter the good or service and the price
    if option == 1 or option == 2 or option ==3:
        goods_Or_Service = input("Enter the good or service for the expense type (" + expense_Type + "):\n")
        price = float(input('Enter the price of the good or the service: \n'))
        today = date.today()
        add_expense(goods_Or_Service, price, today, expense_Type)

# Print a new line
    print()
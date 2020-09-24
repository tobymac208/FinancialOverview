from IncomeInfo import IncomeItem
from IncomeInfo import IncomeItemList
from DebtInfo import DebtItem
from DebtInfo import DebtItemList
from FinancialOverview import FinancialOverview
import os

# read in the income and debt data
# return a new instance of that object with the specified name
def read_data(name_of_overview):
    object = FinancialOverview(name_of_overview)
    with open("income.txt", 'r', encoding = 'utf-8') as file:
        # load in income data
        for line in file:
            split_string = line.split(',')
            # use the data to create a new IncomeItem
            new_income_item = IncomeItem(split_string[0], float(split_string[1]))
            # add the new item
            object.add_income_item(new_income_item)
    with open('debt.txt', 'r', encoding='utf-8') as file:
        for line in file:
            split_string = line.split(',')
            new_debt_item = DebtItem(split_string[0], float(split_string[1]))
            object.add_debt_item(new_debt_item)
    return object
def write_data(object):
    if not isinstance(object, FinancialOverview):
        raise TypeError('wrong type')
    with open('income.txt', 'w', encoding = 'utf-8') as file:
        for entry in object.get_income_list():
            file.write('{},{}\n'.format(entry.get_name(), entry.get_amount()))
    with open('debt.txt', 'w', encoding = 'utf-8') as file:
        # write data
        for entry in object.get_debt_list():
            file.write('{},{}\n'.format(entry.get_name(), entry.get_amount()))  

# Setup our main object
overview = read_data("Nik's finances for the month of September 2020")

# print the menu
# TODO: Finish
while True:
    # clear the screen
    os.system('clear')

    # print out the info
    overview.print_overview()
    
    user_input = int(input('(1) income, (2) debt, (3) exit: '))
    if user_input is 1:
        user_input = int(input('(1) add, (2) back: '))
        # check the input
        if user_input is 1:
            # create a new income item
            print('create new income item: ')
            income_name = input('name: ')
            income_amount = float(input('amount: '))
            new_item = IncomeItem(income_name, income_amount)
            overview.add_income_item(new_item)
            continue
        elif user_input is 2:
            continue
    if user_input is 2:
        user_input = int(input('(1) add, (2) back: '))
        # check the input
        if user_input is 1:
            # create a new income item
            print('create new debt item: ')
            income_name = input('name: ')
            income_amount = float(input('amount: '))
            new_item = DebtItem(income_name, income_amount)
            overview.add_debt_item(new_item)
            continue
    # leave the loop
    elif user_input is 3:
        print('exiting...')
        break

# write data out to files
write_data(overview)
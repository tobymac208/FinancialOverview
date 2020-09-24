from IncomeInfo import IncomeItem
from IncomeInfo import IncomeItemList
from DebtInfo import DebtItem
from DebtInfo import DebtItemList
from FinancialOverview import FinancialOverview

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

# Setup our main object
overview = read_data("Nik's finances for the month of September 2020")

# print out the info
overview.print_overview()

# write data out to files
# TODO: Write data
with open('income.txt', 'w', encoding = 'utf-8') as file:
    # write data
    for entry in overview.get_income_list():
        file.write('{},{}'.format(entry.get_name(), entry.get_amount()))
with open('debt.txt', 'w', encoding = 'utf-8') as file:
    # write data
    for entry in overview.get_debt_list():
        file.write('{},{}'.format(entry.get_name(), entry.get_amount()))
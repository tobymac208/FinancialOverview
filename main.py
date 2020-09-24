from IncomeInfo import IncomeItem
from IncomeInfo import IncomeItemList
from DebtInfo import DebtItem
from DebtInfo import DebtItemList
from FinancialOverview import FinancialOverview

# Setup our main object
overview = FinancialOverview("Nik's finances for the month of September 2020")

# load in data
with open("income.txt", 'r', encoding = 'utf-8') as file:
    # load in income data
    for line in file:
        split_string = line.split(',')
        # use the data to create a new IncomeItem
        new_income_item = IncomeItem(split_string[0], float(split_string[1]))
        # add the new item
        overview.add_income_item(new_income_item)
with open('debt.txt', 'r', encoding='utf-8') as file:
    for line in file:
        split_string = line.split(',')
        new_debt_item = DebtItem(split_string[0], float(split_string[1]))
        overview.add_debt_item(new_debt_item)

# get some income items ready
# income_item_one = IncomeItem("Alexander Home Services", 530.83)
# income_item_two = IncomeItem("Alexander Home Services", 387.45)

# get some debt items ready
# debt_item_one = DebtItem("Next Level Combat", 130.00)
# debt_item_two = DebtItem("Next Insurance", 62.30)
# debt_item_three = DebtItem("Hulu", 12.00)
# debt_item_four = DebtItem("Gym", 30.00)

# add the items to the object
# overview.add_income_item(income_item_one)
# overview.add_income_item(income_item_two)

# overview.add_debt_item(debt_item_one)
# overview.add_debt_item(debt_item_two)
# overview.add_debt_item(debt_item_three)
# overview.add_debt_item(debt_item_four)

# print out the info
overview.print_overview()

# write data out to files
# TODO: Write data
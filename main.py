from IncomeInfo import IncomeItem
from IncomeInfo import IncomeItemList
from DebtInfo import DebtItem
from DebtInfo import DebtItemList
from FinancialOverview import FinancialOverview

# Setup our main object
overview = FinancialOverview("Nik's finances for the month of September 2020")

# get some income items ready
income_item_one = IncomeItem("Alexander Home Services", 530.83)
income_item_two = IncomeItem("Alexander Home Services", 387.45)

# get some debt items ready
debt_item_one = DebtItem("Next Level Combat", 130.0)
debt_item_two = DebtItem("Next Insurance", 62.30)
debt_item_three = DebtItem("Hulu", 12.00)

# add the items to the object
overview.add_income_item(income_item_one)
overview.add_income_item(income_item_two)
overview.add_debt_item(debt_item_one)
overview.add_debt_item(debt_item_two)
overview.add_debt_item(debt_item_three)

# print out the info
overview.print_overview()
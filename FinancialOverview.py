from IncomeInfo import IncomeItem
from IncomeInfo import IncomeItemList
from DebtInfo import DebtItemList
from DebtInfo import DebtItem

class FinancialOverview:
    name = ""
    income_info = IncomeItemList()
    debt_info = DebtItemList()

    def __init__(self, name):
        self.name = name

    # methods for adding an item to the respective lists
    def add_income_item(self, income_item):
        if not isinstance(income_item, IncomeItem):
            raise TypeError('argument must be of type IncomeItem')
        self.income_info.add_item(income_item)
    def add_debt_item(self, debt_item):
        if not isinstance(debt_item, DebtItem):
            raise TypeError('argument must be of type DebtItem')
        self.debt_info.add_item(debt_item)
    
    # prints the overview of your monthly financial situation
    def print_overview(self):

        iteration_count = 0
        total_paid = 0.0
        # print and calulcate the income info
        print()
        print("*** Amount paid ***")
        for value in range(len(self.income_info.get_list())):
            iteration_count += 1
            print("{}. {}".format(iteration_count, self.income_info.get_list()[value].get_info()))
            total_paid += self.income_info.get_list()[value].get_amount()
        print("Total paid: {}\n".format(total_paid))
        
        iteration_count = 0
        total_owed = 0.0
        # print and calulcate the debt info
        print("*** Amount owed ***")
        for value in range(len(self.debt_info.get_list())):
            iteration_count += 1
            print("{}. {}".format(iteration_count, self.debt_info.get_list()[value].get_info()))
            total_owed += self.debt_info.get_list()[value].get_amount()
        print("Total owed: {}\n".format(total_owed))
        
        # Print the overall amount left
        print("Net proft for this month: {}".format(total_paid - total_owed))
        # Print the percentage of income going away
        print("percentage of income being used: {}%".format(round(100 * (total_owed/total_paid))))

# an amount of income
class IncomeItem:
    source_of_income = ""
    amount = 0.0

    def __init__(self, source_of_income, amount):
        self.source_of_income = source_of_income
        # verify the input in valid
        if not isinstance(amount, float):
            raise TypeError("'amount' argument must be a float")
        self.amount = amount
    
    # return a "tostring" of the item
    def get_info(self):
        return self.source_of_income + ": " + str(self.amount)

    def get_amount(self):
        return self.amount

class IncomeItemList:
    list_of_items = []

    def add_item(self, item):
        # verify that it's the right data type
        if not isinstance(item, IncomeItem):
            raise TypeError("argument must be of type IncomeItem")
        self.list_of_items.append(item)
    
    # returns the local list of items
    def get_list(self):
        return self.list_of_items
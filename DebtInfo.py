class DebtItem:
    name = ""
    amount = 0.0

    def __init__(self, name, amount):
        self.name = name
        if not isinstance(amount, float):
            raise TypeError("amount argument must be of type float")
        self.amount = amount
    def get_info(self):
        return self.name + ": " + str(self.amount)

    def get_amount(self):
        return self.amount

class DebtItemList:
    list_of_owed = []

    # add an item, making sure it's a valid type
    def add_item(self, item):
        if not isinstance(item, DebtItem):
            raise TypeError("item must be of type FinancialInfo")
        self.list_of_owed.append(item)
    
    # give the user a detailed list of their financial situation
    def print_overview(self):
        count = 0
        cost = 0.0
        for i in range(len(self.list_of_owed)):
            count += 1
            print(str(count) + ". " + self.list_of_owed[i].print_info())
            # calculate the total cost/month
            cost += self.list_of_owed[i].get_amount()
        # print the total cost
        print("Total owed: " + str(cost))

    def get_list(self):
        return self.list_of_owed

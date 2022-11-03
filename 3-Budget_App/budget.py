class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        
    #Format class string prints such that category is centered, 23 chars from description, 7 ints for amount and 2 float decimals, finally, print the balance. 
    def __str__(self):
        p_string = f"{self.category.center(30, '*')}\n"
        for items in self.ledger:
            tmp = f"{items['description'][:23]:23}{items['amount']:7.2f}"
            p_string += f"{tmp}\n"
        p_string += f"Total: {self.get_balance()}"
        return p_string

    def deposit(self, amount, description=""):
        tmp = {'amount': amount, 'description': description}        #Create dictionary with amount and description
        self.ledger.append(tmp)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            tmp = {'amount': 0-amount, 'description': description}        #Create dictionary with amount and description
            self.ledger.append(tmp)
            return True
        return False

    def get_balance(self):
        balance = 0
        for items in self.ledger:
            balance += items['amount']
        return balance
    
    def transfer(self, amount, category_dif):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_dif.category}")
            category_dif.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
    
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True

def create_spend_chart(cat_list):
    #Create empty list, if the amount in the each category, passed with cat_list is less than zero (withdraw), add it to tmp variable and append it to list. Totalt will be the sum of all list elements.
    spent_tot = []
    percentage = []
    for category in cat_list:
        tmp_tot = 0
        for items in category.ledger:
            if items['amount'] < 0:
                tmp_tot += abs(items['amount'])
        spent_tot.append(tmp_tot)
    
    #Calculate the percentage spent by category
    for i in spent_tot:
        percentage.append((i*100)/sum(spent_tot))
        
    #Generate bar char
    bar_str = "Percentage spent by category"
    for i in range(100, -1, -10):    #Create percentage
        bar_str += f"\n{str(i).rjust(3)}|"
        for percent in percentage:
            if percent > i:
                bar_str += " o "
            else:
                bar_str += "   "
        bar_str += " "
    bar_str += "\n    ----------"
    
    #Category formatting
    cat = []
    for category in cat_list:
        cat.append(len(category.category))
    
    for i in range(max(cat)):
        bar_str += "\n     "
        for category in range(len(cat_list)):
            if i < cat[category]:
                bar_str += f"{cat_list[category].category[i]}  "
            else:
                bar_str += "   "
    
    return bar_str
class BudgetCategory:
    

    def __init__ (self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.expenses = 0

    def get_category(self):
        return self.__category_name
    
    def get_budget(self):
        return self.__allocated_budget
    
    def set_category(self, new_category):
        self.__category_name = new_category

    def set_budget(self, new_budget):
        self.__allocated_budget = new_budget

    def add_expense(self, amount):
        if 0 < amount <= self.__allocated_budget:
            self.set_budget(self.get_budget() - amount)
            self.expenses += amount
        else:
            print('You are outside of your budget.')
        
    def display_details(self):
        print(f'The {self.__category_name} category started at {self.__allocated_budget + self.expenses} but has a remainder of {my_budget.get_budget()}')        


my_budget = BudgetCategory('Food', 200)

my_budget.add_expense(100)
# my_budget.set_category('Gas')

print(f'I am allowed to spend {my_budget.get_budget()}, on {my_budget.get_category()}')

my_budget.display_details()
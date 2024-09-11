import budget
outgoings = budget.BudgetManager(2500)
outgoings.add_budget("Groceries", 500)
outgoings.print_summary()

def change_budget(self, name, new_amount):
        if name not in self.budgets:
            raise ValueError("Budget does not exists")
        old_amount = self.budgets[name]
        if new_amount > old_amount + self.available:
            raise ValueError("Insufficient funds")
        self.budgets[name] = new_amount
        self.available -= new_amount - old_amount
        return self.available
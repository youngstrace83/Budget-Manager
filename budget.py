available = 2500.00
budgets = {}
expenditure = {}

def add_budget(name, amount):
    global available
    budgets[name] = amount
    available -= amount
    expenditure[name] = 0
    return available
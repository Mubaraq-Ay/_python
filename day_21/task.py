class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []

    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})

    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income['amount']
        return total


p1 = PersonAccount("Mubaraq", "Ayinde")
p1.add_income(50000, "salary")
p1.add_income(10000, "side hustle")
print(p1.total_income())   # should print 60000
class TaxCalculator():
    def __init__(self,salary):
        self.Summary = salary*12
        print(f"Annual Income = {self.Summary}")
    def PersonalExpense(self,Cost):
        if Cost < 6000 :self.Summary -= Cost
        else:self.Summary -= - 6000
        print(f"Summary = {self.Summary}")
    def ChildExpense(self,Cost):
        if Cost < 120000 :self.Summary -= Cost
        else:self.Summary -= 120000
        print(f"Summary = {self.Summary}")
    def FamilyInsurance(self,Cost):
        if Cost < 100000 :self.Summary -= Cost
        else:self.Summary -= 100000
        print(f"Summary = {self.Summary}")
    def ParentCare(self):
        PC = [[],[]]
        n = int(input("Enter Parent Count :"))
        for i in range(1,n+1):
            PC[0].append(int(input(f"Parent{i}'s Age = ")))
            PC[1].append(int(input(f"Parent{i}'s Expense = ")))
        for i in range(0,n):
            if PC[0][i] >= 60:
                if PC[1][i] < 100000:self.Summary -= PC[1][i]
                else: self.Summary -= 100000
        print(f"Summary = {self.Summary}")
    def HousePay(self,Cost):
        if Cost < 100000 :self.Summary -= Cost
        else:self.Summary -= 100000
    def TaxCost(self):
        if self.Summary <= 300000: self.tax = 0
        elif self.Summary <= 450000: self.tax = self.Summary * 3.5 /100
        elif self.Summary <= 600000: self.tax = self.Summary * 5 /100
        elif self.Summary <= 800000: self.tax = self.Summary * 7 /100
        else: self.tax = self.Summary / 10
        print(f"Tax = {self.tax}")
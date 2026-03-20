class TaxTable():
    def __init__(self,taxRange,taxPrice,Income):
        self._taxRange = taxRange
        self._taxPrice = taxPrice
        self._income = Income
        self.sumTax = 0
class TaxCalculate(TaxTable):
    def calculate(self):
        i = 0
        while self._income > 0:
            if (i<7) and (self._income >= self._taxRange[i]):
                self.sumTax += self._taxRange[i]*self._taxPrice[i]
                self._income -= self._taxRange[i]
            else:
                self.sumTax += self._income*self._taxPrice[i]
                self._income-=self._income
            i += 1
        print(f"Your tax = {self.sumTax}")

n = int(input("Yeary Income :"))
taxRange = [150000,150000,200000,250000,250000,1000000,3000000]
taxPrice = [0,0.05,0.10,0.15,0.20,0.25,0.30,0.35]    
A =TaxCalculate(taxRange,taxPrice,n)
A.calculate()
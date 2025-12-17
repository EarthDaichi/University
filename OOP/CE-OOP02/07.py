class USDTHB:
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency
    def to_USD(self):
        if self.currency == 'THB':
            self.currency = 'USD'
            self.amount = self.amount/35
            return self.amount/35
        else:
            return self.amount
    def to_THB(self):
        if self.currency == 'USD':
            self.currency = 'THB'
            self.amount = self.amount*35
            return self.amount*35
        else:
            return self.amount
        
money = USDTHB(34232,'THB')
print(money.amount, money.currency)
money.to_THB()
print(money.amount, money.currency)
money.to_USD()
print(money.amount, money.currency)
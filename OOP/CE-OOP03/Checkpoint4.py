class exchangeMoney:
    def __init__(self ,money):
        self.money = money
    def exchange(self):
        print('Thai-Bath convert to USD = ', self.money/36, 'Dollars')
        print('Thai-Bath convert to JPY = ', self.money*25/100, 'Yen')
        print()

print("-"*20)
print('''Hello, I'm an exchange money program''')
print('''I'm able to convert Thai-bath to other currency''')
m = float(input("Enter your amount of Thai money : "))

op = exchangeMoney(m)
op.exchange()
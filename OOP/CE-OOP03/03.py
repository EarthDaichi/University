class exchangeMoney:
    def __init__(self , choice , money):
        self.choice = choice
        self.money = money
    def exchange(self):
        if self.choice == 1:
            print('Thai-Bath convert to USD = ', self.money/36, 'Dollars')
            print()
            print('Thai-Bath convert to JPY = ', self.money*25/100, 'Yen')
            print()

print("-"*20)
print('''Hello, I'm an exchange money program''')
print('''I'm able to convert Thai-bath to other currency''')
print("-"*20)
print('''Press 1: Thai-Bath to US-Dollar''')
print('''Press 2: Thai-Bath to Japan-Yen''')
print("-"*20)
m = float(input("Enter your amount of Thai money : "))
c = int(input("Enter your choice : "))

op = exchangeMoney(c , m)
op.exchange()
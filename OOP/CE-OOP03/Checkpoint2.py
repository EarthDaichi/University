class Star: 
    def __init__(self,n):
        self.n = n
    def star01(self):
        for i in range(self.n):
            for j in range(self.n):
                if j > i:
                    print(' ', end = ' ')
                else:
                    print('*', end = ' ')
            print()
        print()
    def star02(self):
        for i in range(self.n):
            for j in range(self.n):
                if j >= i:
                    print(' ', end = ' ')
                else:
                    print('*', end = ' ')
            print()
    def star03(self):
        for i in range(self.n):
            for  j in range(self.n):
                if j+i >=self.n :
                    print('*', end = ' ')
                else:
                    print(' ', end = ' ')
            print()
        
s = Star(5)
s.star01()
s.star02()
s.star03()
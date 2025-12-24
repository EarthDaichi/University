class Star: 
    def __init__(self,n):
        self.n = n
class star1(Star):
    def star01(self):
        for i in range(self.n):
            for j in range(self.n):
                if j > i:
                    print(' ', end = ' ')
                else:
                    print('*', end = ' ')
            print()
        print()
class star2(Star):
    def star02(self):
        for i in range(self.n):
            for j in range(self.n):
                if j >= i:
                    print(' ', end = ' ')
                else:
                    print('*', end = ' ')
            print()
class star3(Star):
    def star03(self):
        for i in range(self.n):
            for  j in range(self.n):
                if j+i >=self.n :
                    print('*', end = ' ')
                else:
                    print(' ', end = ' ')
            print()
        
s1 = star1(5)
s1.star01()
s2 = star2(7)
s2.star02()
s3 = star3(9)
s3.star03()
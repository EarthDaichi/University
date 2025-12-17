class prime:
    def input(self,n):
        self.n = n
    def result(self):
        for i in range(2,self.n):
            if self.n%i == 0:
                print(self.n, "is  not a prime number")
                break
            else:
                print(self.n, "is a prime number")
                
Number1 = prime()
Number1.input(int(input("Enter a number : ")))
Number1.result()
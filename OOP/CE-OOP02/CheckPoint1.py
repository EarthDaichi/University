class multiply:
    def input(self,n):
        self.n = n
    def calculate(self):
        for i in range(13):
            print(f"{self.n} * {i} = {self.n*i}")
            
result = multiply()
result.input(int(input("Enter a number : ")))
result.calculate()
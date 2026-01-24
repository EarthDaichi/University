class Multiply:
    def __init__(self,x):
        self.x = x
    def __showMultiply(self):
        for i in range(1,13):
            print(f"{self.x} x {i} = {self.x*i}")

m = Multiply(10)
m.showMultiply()
class Stat:
    sum = 0
    def __init__(self, listZ):
        self.listZ = listZ
    def Summation(self):
        for i in self.listZ:
            Stat.sum = Stat.sum+i
        print("Summation = " ,Stat.sum)
    def Average(self):
        print("Average = ", Stat.sum/len(self.listZ))
    def __del__(self):
        print("----- Program terminated -----")

data = [10, 15, 20, 25, 30]
s = Stat(data)
s.Summation()
s.Average()
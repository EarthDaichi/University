class Stat:
    sum = 0
    def Summation(self,listZ):
        self.listZ = listZ
        for i in range(len(self.listZ)):
            Stat.sum = Stat.sum+data[i]
        print(Stat.sum)
    def Average(self):
        print("Average = ", Stat.sum/len(self.listZ))


data = [10, 15, 20, 25, 30]
s = Stat()
s.Summation(data)
s.Average()
class Data:
    def __init__(self, listData):
        self._Data = listData
class Summation(Data):
    def Sum(self):
        print("Summation = " , sum(self._Data))
class Average(Summation):
    def Avg(self):
        print("Average = ", sum(self._Data)/len(self._Data))
class Maximum(Data):
    def Max(self):
        print("Maximum value = ", max(self._Data))
class Minimum(Data):
    def Min(self):
        print("Minimum value =", min(self._Data))

A = [10, 15, 20, 25, 30]
x = Average(A)
x.Sum()
x.Avg()
y = Maximum(A)
y.Max()
z = Minimum(A)
z.Min()
class Data:
    def __init__(self, listData):
        self._Data = listData
class Summation(Data):
    sum = 0
    def Sum(self):
        for i in range(len(self._Data)):
            Summation.sum = Summation.sum+self._Data[i]
        print("Summation = " ,Summation.sum)
class Average(Summation):
    def Avg(self):
        print("Average = ", Summation.sum/len(self._Data))
class Maximum(Data):
    def Max(self):
        max = self._Data[0]
        for i in self._Data:
            if max < i:
                max = i
            else:
                max = max
        print("Maximum value = ", max)
class Minimum(Data):
    def Min(self):
        min = self._Data[0]
        for i in self._Data:
            if min > i:
                min = i
            else:
                min = min
        print("Minimum value =", min)

A = [10, 15, 20, 25, 30]
x = Average(A)
x.Sum()
x.Avg()
y = Maximum(A)
y.Max()
z = Minimum(A)
z.Min()
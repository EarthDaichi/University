class Data:
    def __init__(self,listData):
        self._Data = listData
        self._sum = 0
class Summation(Data):
    def Sum(self):
        for i in self._Data:
            self._sum += i
        print("Summation = ", self._sum)
    def __del__(self):
        print("Program terminated")
class Average(Summation):
    def Avg(self):
        print("Average = ", self._sum/len(self._Data))
    def __del__(self):
        print("Program terminated")
class Maximum(Data):
    def Max(self):
        max = self._Data[0]
        for i in self._Data:
            if max < i:
                max = i
            else:
                max = max
        print("Maximum value = ", max)
    def __del__(self):
        print("Program terminated")
class Minimum(Data):
    def Min(self):
        min = self._Data[0]
        for i in self._Data:
            if min < i:
                min = i
            else:
                min = max
        print("Minimum value = ", min)
    def __del__(self):
        print("Program terminated")
class Sorting(Data):
    def LesstoMost(self):
        print("Less to Most : ", sorted(self._Data))
    def MosttoLess(self):
        print("Most to Less : ", sorted(self._Data, reverse = True))
    def __del__(self):
        print("Program terminated")
        
A = [10, 15 ,20, 25, 30]
x = Sorting(A)
x.MosttoLess(); x.LesstoMost()
x = Average(A)
x.Sum(); x.Avg()
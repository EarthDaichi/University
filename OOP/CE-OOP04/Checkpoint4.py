class Data:
    def __init__(self, listData):
        self._Data = listData
        self._sum = 0
class Summation(Data):
    def Sum(self):
        for i in self._Data:
            self._sum = self._sum+i
        print("Summation = ", self._sum)
class Average(Summation):
    def Avg(self):
        print("Average = ", self._sum/len(self._DAta))
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
        print("Minimum value = ", min)
class Sorting(Data):
    def LesstoMost(self):
        print("Less to Most", sorted(self._Data))
    def MosttoLess(self):
        print("Most to Less", sorted(self._Data, reverse = True))
class Search(Data):
    def find(self,num):
        for i in self._Data:
            if i == num:
                print(f"Number ({num}) is found")
                return 0
        print(f"Number ({num}) is not found")
        
A = [10 , 15 , 20 , 25 , 30]
x = Sorting(A)
x.MosttoLess()
x.LesstoMost()
S = Search(A)
S.find(30)
S.find(7)
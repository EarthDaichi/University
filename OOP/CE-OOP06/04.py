import math
data = [42,20,64,51,34,70,31,16,15,12,19,33]

class SetUp():
    def __init__(self,input_):
        self._sum = 0
        self._list = input_
        for i in self._list:
            self._sum += i
class Calculate(SetUp):
    def summation(self):
        print(f"Summation = {self._sum}")
    def average(self):
        self._count = 0
        for i in self._list:
            self._count += 1
        self._avg = self._sum/self._count
        print(f"Average = {self._avg}")
    def maximum(self):
        self._Mm = 0
        for i in self._list:
            if i > self._Mm: self._Mm = i
        print(f"Maximum number = {self._Mm}")
    def minimum(self):
        self._mm = math.inf
        for i in self._list:
            if i < self._mm : self._mm = i
        print(f"Minimum number = {self._mm}")
    def Sort(self):
        print(f"sort = {sorted(self._list,reverse=(int(input("Sorter : enter 1 for Ascending or 0 for Descending :\n"))))}")

A = Calculate(data)
A.summation()
A.average()
A.maximum()
A.minimum()
A.Sort()
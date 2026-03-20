import random
import statistics

class theData:
    def __init__(self,myData):
        self._myData = myData
    def Display(self):
        print(self._myData)
class theSummation(theData):
    def mySummation(self):
        self._mySum = sum(self._myData); print("Summation = ", self._mySum)
class theMean(theData):
    def myMean(self):
        self._Mean = sum(self._myData)/len(self._myData); print("Mean = ", self._Mean)
class theMax(theData):
    def myMaximum(self):
        self._myMax = max(self._myData); print("Maximum = ", self._myMax)
class theMin(theData):
    def myMinimum(self):
        self._myMin = min(self._myData); print("Minimum = ", self._myMin)
class theVariance(theData):
    def myVariance(self):
        self._myVar = statistics.variance(self._myData); print("Variance = ", self._myVar)
class theSD(theData):
    def mySD(self):
        self._SD = statistics.stdev(self._myData); print("Standard Deviation = ", self._SD)
class theSort(theData):
    def mySort(self):
        self._mySort = sorted(self._myData); print("Sorted = ", self._mySort)
class theMedian(theSort):
    def myMedian(self):
        self._myCount = len(self._myData); self._mySort = sorted(self._myData)
        self._myMedian = self._mySort[int(self._myCount/2)]; print("Median = ", self._myMedian)
        
myData = [random.randint(1,100) for i in range(12)]
I_need_to_know = theData(myData); I_need_to_know.Display()
I_need_to_know = theSummation(myData); I_need_to_know.mySummation()
I_need_to_know = theMean(myData); I_need_to_know.myMean()
I_need_to_know = theMax(myData); I_need_to_know.myMaximum()
I_need_to_know = theMin(myData); I_need_to_know.myMinimum()
I_need_to_know = theVariance(myData); I_need_to_know.myVariance()
I_need_to_know = theSD(myData); I_need_to_know.mySD()
I_need_to_know = theSort(myData); I_need_to_know.mySort()
I_need_to_know = theMedian(myData); I_need_to_know.myMedian()
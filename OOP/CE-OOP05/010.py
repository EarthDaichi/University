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
        
myData = [42,20,64,51,34,70,31,16,15,12,19,33]
I_need_to_know = theData(myData); I_need_to_know.Display()
I_need_to_know = theSummation(myData); I_need_to_know.mySummation()
I_need_to_know = theMean(myData); I_need_to_know.myMean()
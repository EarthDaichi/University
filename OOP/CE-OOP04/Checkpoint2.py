import numpy as np

class MATRIX:
    def __init__(self, listA , listB , listD):
        self._listA = listA
        self._listB = listB
        self._listC = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self._listD = listD
class MultiplyMatrix(MATRIX):
    def _MultiplyMatrix(self):
        self._listA = np.array(self._listA)
        self._listB = np.array(self._listB)
        self._listC = self._listA @ self._listB
        for r in self._listC:
            print(r)
class Matrix_Det(MATRIX):
    def Determinant(self):
        det = np.linalg.det(self._listD)
        print("Determinant is = ", det)
class Matrix_Tps(MATRIX):
    def set(self,tps):
        self.tps = tps
        if tps == "a" or tps == "A":
            self._PreTpsList = [i[:] for i in self._listA]
            self._TpsList = [i[:] for i in self._listA]
        elif tps == "b" or tps == "B":
            self._PreTpsList = [i[:] for i in self._listB]
            self._TpsList = [i[:] for i in self._listB]
        elif tps == "d" or tps == "D":
            self._PreTpsList = [i[:] for i in self._listD]
            self._TpsList = [i[:] for i in self._listD]
            
    def Transpose(self):
        for i in range (len(self._PreTpsList)):
            for j in range (len(self._PreTpsList[i])):
                self._TpsList[j][i] = self._PreTpsList[i][j]
        print(f"Transpose of {self.tps} is")
        for i in self._TpsList:
            print(i)
            
a = [[4,1,7],
     [2,4,8],
     [3,7,1]]
b = [[6,8,1],
     [9,7,5],
     [2,4,3]]
d=  [[5,2,1,4,6],
     [9,4,2,5,2],
     [11,5,7,3,9],
     [5,6,6,7,2],
     [7,5,9,3,3]]

OOP = MultiplyMatrix(a,b,d)
OOP._MultiplyMatrix()
OOR = Matrix_Det(a,b,d)
OOR.Determinant()
TpsA = Matrix_Tps(a,b,d);  TpsA.set("a");  TpsA.Transpose()
TpsB = Matrix_Tps(a,b,d);  TpsB.set("B");  TpsB.Transpose()
TpsD = Matrix_Tps(a,b,d);  TpsD.set("D");  TpsD.Transpose()
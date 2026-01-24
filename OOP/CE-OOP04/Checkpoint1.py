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
        for i in range(len(self._listA)):
            for j in range (len(self._listB[0])):
                for k in range(len(self._listB)):
                    self._listC[i][j] += self._listA[i][k] * self._listB[k][j]
        for r in self._listC:
            print(r)
class Matrix_Det(MATRIX):
    def Determinant(self):
        det = np.linalg.det(self._listD)
        print("Determinant is = ", det)
class Matrix_tp(MATRIX):
    def Transpose(self):
        for i in range (len())
        print("Transpose is")
        for i in tp:
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
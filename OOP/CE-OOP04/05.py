class MATRIX:
    def __init__(self, listA , listB):
        self._listA = listA
        self._listB = listB
        self._listC = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
class MultiplyMatrix(MATRIX):
    def _MultiplyMatrix(self):
        for i in range(len(self._listA)):
            for j in range (len(self._listB[0])):
                for k in range(len(self._listB)):
                    self._listC[i][j] += self._listA[i][k] * self._listB[k][j]
        for r in self._listC:
            print(r)
            
a = [[4,1,7],
     [2,4,8],
     [3,7,1]]
b = [[6,8,1],
     [9,7,5],
     [2,4,3]]

OOP = MultiplyMatrix(a,b)
OOP._MultiplyMatrix()
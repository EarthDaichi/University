class MATRIX:
    def __init__(self, listA , listB):
        self.listA = listA
        self.listB = listB
        self.listC = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
    def _MultiplyMatrix(self):
        for i in range(len(self.listA)):
            for j in range (len(self.listB[0])):
                for k in range(len(self.listB)):
                    self.listC[i][j] += self.listA[i][k] * self.listB[k][j]
        for r in self.listC:
            print(r)
            
a = [[4,1,7],
     [2,4,8],
     [3,7,1]]
b = [[6,8,1],
     [9,7,5],
     [2,4,3]]

OOP = MATRIX(a,b)
OOP._MultiplyMatrix()
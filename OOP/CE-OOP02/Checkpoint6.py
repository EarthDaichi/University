class MultiplyMatrix:
    def __init__(self,lista,listb):
        self.a = lista
        self.b = listb
        self.c = [[0,0,0],[0,0,0],[0,0,0]]
    
    def multiply(self):
        for i in range((len(a)) ):
            for j in range((len(b[0])) ):
                for k in range(len(b)):
                    self.c[i][j] += a[i][j] * b[i][j]        
        for r in self.c:
            print(r)

a = [[4,1,7],[2,4,8],[3,7,1]]
b = [[6,8,1],[9,7,5],[2,4,3]]

Result1 = MultiplyMatrix(a,b)
Result1.multiply()
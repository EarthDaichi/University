class jumpball:
    def height(self,h):
        self.h = h
    def decrease(self):
        self.h = self.h *0.9
        

Ball1 = jumpball()
count = 0
Ball1.height(int(input("Enter height : ")))

while Ball1.h > 0.1:
    Ball1.decrease()
    count += 1
print(f"Ball Bounce = {count} Times")
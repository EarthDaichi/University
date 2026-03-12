class workers():
    def __init__(self,HP=100,money=0,happiness=0):
        self.HP = HP
        self.money = money
        self.happiness = happiness
    def report(self):
        print(f"HP : {self.HP}")
        print(f"money : {self.money}")
        print(f"happiness : {self.happiness}")
    def work(self):
        self.money += 200
        self.happiness += 100
        self.HP -= 70
        self.report()
    def sleep(self):
        self.money -= 100
        self.happiness += 150
        self.HP += 300
        self.report()
    def play(self):
        self.money -= 100
        self.HP -= 100
        self.happiness += 250
        self.report()
MrKhaYun = workers(100,0,0)
MrKhaYun.report()
print("-"*20)
MrKhaYun.work()
print("-"*20)
MrKhaYun.sleep()
print("-"*20)
MrKhaYun.play()
class Warrior:
    def __init__(self,power,defense,HP=100):
        self.power = power
        self.defense = defense
        self.HP = HP
    def attack(self,warrior_object):
        if self.power <= warrior_object.defense:
            print(f"{warrior_object}'s HP = {warrior_object.HP}")
        elif self.power > warrior_object.defense:
            warrior_object.HP = warrior_object.HP - (self.power - warrior_object.defense)
            if warrior_object.HP >0:
                print(f"Enemy's HP = {warrior_object.HP}")
            else:
                print(f"Enemy died")

Player1 = Warrior(135,40,100)
Player2 = Warrior (60,25,100)

print("Player1 attack : ")
Player1.attack(Player2)
print("Player2 attack : ")
Player2.attack(Player1)
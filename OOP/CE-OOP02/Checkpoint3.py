class grader:
    def score(self,s):
        self.s = s
    def result(self):
        if self.s >=  80:
            print("You got grade A")
        elif self.s >=  75:
            print("You got grade B+")
        elif self.s >=  70:
            print("You got grade B")
        elif self.s >=  65:
            print("You got grade C+")
        elif self.s >=  60:
            print("You got grade C")
        elif self.s >=  55:
            print("You got grade D+")
        elif self.s >=  50:
            print("You got grade D")
        else:
            print("You got grade F, see you agian next term")

Student1 = grader()
Student1.score(float(input("Enter your score : ")))
Student1.result()
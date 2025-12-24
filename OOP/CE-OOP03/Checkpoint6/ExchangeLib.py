class trade:
    def __init__(self,m):
        self.money1 = m
    def exchange(self,choice1,choice2):
        if choice1 == choice2:
            print("Can not exchange to the same currency")
            return 0
        #----------------------
        if choice1 == 1:self.currency1 = "Thai-Bath";self.medium = self.money1/31.07
        elif choice1 == 2:self.currency1 = "US-Dollar";self.medium = self.money1
        elif choice1 == 3:self.currency1 = "Euro";self.medium = self.money1*1.18
        elif choice1 == 4:self.currency1 = "Japan-Yen";self.medium = self.money1/156.02
        elif choice1 == 5:self.currency1 = "Chinese- Yuan";self.medium = self.money1/7.01
        elif choice1 == 6:self.currency1 = "Russia-Ruble";self.medium = self.money1/79
        #----------------------    
        if choice2 == 1:self.currency2 = "Thai-Bath";self.money2 = self.medium*31.07
        elif choice2 == 2:self.currency2 = "US-Dollar";self.money2 = self.medium
        elif choice2 == 3:self.currency2 = "Euro";self.money2 = self.medium/1.18
        elif choice2 == 4:self.currency2 = "Japan-Yen";self.money2 = self.medium*156.02
        elif choice2 == 5:self.currency2 = "Chinese- Yuan";self.money2 = self.medium*7.01
        elif choice2 == 6:self.currency2 = "Russia-Ruble";self.money2 = self.medium*79
        
        print(f"{self.money1} {self.currency1} = {self.money2:.2f} {self.currency2}")
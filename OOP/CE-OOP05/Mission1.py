while 1:
    class InstallmentInfo():
        def __init__(self,price,interest,time):
            self._price = price
            self._interest = interest
            self._time = time
    class CarInstallMent(InstallmentInfo):
        def Calculate(self):
            if (2.19 <= self._interest <= 5.75):
                if (3 <= self._time <= 7):
                    self._cost = self._price * (self._interest/100) * self._time
                    print(f"your car total cost = {self._cost:.2f}")
                else: print("Error: Time must be between 3 and 7")
            else: print("Error: interest must be between 2.19 and 5.75")
                
    price = int(input("Enter price of car : "))
    interest = float(input("Enter Installment interest : "))
    time = int(input("Enter Installment Duration : "))

    A = CarInstallMent(price,interest,time)
    A.Calculate()
h = int(input("Enter height : "))
counter = 0
while h > 0.1:
    h = h*0.9
    counter +=1
print("Ball bounce = ", counter , "times")
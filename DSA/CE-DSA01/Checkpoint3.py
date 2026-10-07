import random

data = [random.randint(1,100) for i in range(12)]
print(f"1. data : {data}")

for i in range(3) : data.append(random.randint(1,100))
print(f"2. data : {data}")

data.pop(0); data.pop(2); data.pop(3); data.pop(6); data.pop(7);
print(f"3. data : {data}")

print(f"4. sorted data : {sorted(data)}")
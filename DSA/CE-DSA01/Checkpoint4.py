import random

#  กำหนดค่าให้ Alice ด้วยการสุ่มค่าในช่วง 1-200 จำนวน 12 ตัว
Alice = [random.randint(1,200) for i in range(12)]
#เล่นคำพ้องเสียง A list
print(f"Alice : {Alice}")
#แสดงผลการกำหนดค่า
#คัดลอกข้อมูลจาก Alice มาเก็บใน Blist
Blist  = Alice[:]
print(f"Blist : {Blist}")
#แสดงผลข้อมูลใน Blist
#สุ่มเพิ่มข้อมูลในช่วง 1-200 เข้าไปใน Blist จำนวน 3 รอบ
for i in range(3): Blist.append(random.randint(1,200))
print(f"Blist : {Blist}")
#แสดงผลข้อมูลปัจจุบันใน Blist
#ใช้ Built-in method จัดเรียงค่าใน Blist
Blist.sort()
#แสดงผลค่าที่จัดเรียงแล้ว จาก Blist
print(f"Sorted Blist : {Blist}")
print(f"Sum of Blist = {sum(Blist)}")
#หาค่าผลรวมของข้อมูลใน Blist และแสดงผล
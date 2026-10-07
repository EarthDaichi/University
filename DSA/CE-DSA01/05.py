constellations = ['ชวด','ฉลู','ขาล','เถาะ','มะโรง','มะเส็ง','มะเมีย','มะแม','วอก','ระกา','จอ','กุน']
print(f"ปีนักษัตรทั้ง 12 มีดังนี้ {constellations}")
print("หากต้องการหยุดให้ใส่ค่าน้อยกว่า 1")
while True:
    year = int(input("โปรดใส่ปี พ.ศ. เกิด >> "))
    if(year < 1):
        break

    x = (year+5)%12
    c = constellations[x]
    print(f"คุณตรงกับปีนักษัตร - {c}")
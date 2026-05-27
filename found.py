print("1.Manfiy\n2.Musfat")
a = int(input("Tanlash: "))
if a == 1:
    a < 0
    son_1 = int(input("1-sonni kiriting: "))
    if son_1 < 0:
       print(son_1,"Manfiy son")
    else:
       print("Manfiy emas")
elif a == 2:
    son_2 = int(input("2-sonni kiriting: "))
    if son_2 > 0:
       print(son_2,"Musfat son")
    else:
       print("Musfat emas")
else:
    print("0 ga teng")
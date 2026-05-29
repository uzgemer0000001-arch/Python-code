# javob = ""
# while javob != "chiq":
#     javob = str(input("Yozing: "))
#     print("siz yozdingiz: ", javob)
# print("End")


# parol = str(input("Dasturga parol kiriting: "))
# print(f"{parol} Saqlandi")
# tekshirish = str(input("Kiritgan parolingizni ayting: "))

# while tekshirish != parol:
#     print("Siz yozdingiz", tekshirish)
#     tekshirish = input("Qayta kiriting: ")
# print("Dastur ochildi, parol tug'ri! ")


print("Dasturga xush kelibsiz! ")

urinish = 0

while urinish < 3:

    nom = str(input("Ismingizni kiriting: "))
    parol = str(input("parol kiriting: "))

    print(f"{nom} va {parol} Saqlandi! ")

    tekshirish = str(input("ismingizni kiritng: "))
    tekshirish_2 = str(input("Parolni kiriting: "))

    while tekshirish != nom:

        print("Siz yozdingiz",tekshirish)
        tekshirish = input("Qayta kiriting: ")

    print("Ism tug'ri! parolga uting")  

    while tekshirish_2 != parol:

        print("Siz yozdingiz",tekshirish_2)
        tekshirish_2 = input("Qayta kiriting: ")

    print("Parol tug'ri!") 
    

    urinish += 1

if urinish ==3:
    print("Akaunt bloklandi")
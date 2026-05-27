print("1.+\n2.-\n3.:\n4.*")
a = int(input("Tanlang: "))
if a == 1:
    print("Siz + ni tanladingiz! ")
    son_1 = int(input("Qushiluvchi sonni kiriting: "))
    son_2 = int(input("Qushiladigan sonni kiriting: "))
    Natija = son_1 + son_2
    print("Javob:",Natija,"buladi")
if a == 2:
    print("Siz - ni tanladingiz! ")
    son_1 = int(input("Ayriluvchi sonni kiritng: "))
    son_2 = int(input("Ayriladigan sonni kiriting: "))
    Natija = son_1 - son_2
    print("Javob:",Natija,"buladi")
if a == 3:
    print("Siz : ni tanladingiz! ")
    son_1 = int(input("Bulinadigan sonni kiriting: "))
    son_2 = int(input("Buladigan sonni kiriting: "))
    Natija = son_1 / son_2
    print("Javob:",Natija,"buladi")
if a == 4:
    print("Siz * ni tanladingiz! ")
    son_1 = int(input("Kupaytiriluvchi sonni kiriting: "))
    son_2 = int(input("Kupaytiradigan sonni kiriting: "))
    Natija = son_1 * son_2
    print("Javob:",Natija,"buladi")
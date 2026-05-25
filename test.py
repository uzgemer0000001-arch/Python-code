# for and if,elif,else 
# for i in range(1, 11):
    # if i % 2 != 0:
    #    print(i)

print("1.Juft\n2.Toq")

a = int(input("Tanlash: "))
if a == 1:
    print("Juft son ")
    son_1 = int(input("Boshlangich son: "))
    son_2 = int(input("Tugash son: "))
    for i in range(son_1, son_2):
        if i % 2 == 0:
            print(i, "Juft son")
elif a == 2:
    print("Toq son")
    print("Juft son ")
    son_1 = int(input("Boshlangich son: "))
    son_2 = int(input("Tugash son: "))
    for i in range(son_1, son_2):
        if i % 2 != 0:
            print(i,"Toq son")
else:
    print("error")
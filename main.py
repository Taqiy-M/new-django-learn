#
# import random as r
#
# l = []
# for i in range(0, 100):
#     a = r.randint(-10, 10)
#     l.append(a)
#
#
# print(l)
# # print(l.count(-5))
#
# yettilar = 0
# for i in l:
#     if i == 7:
#         yettilar += 1
# print(yettilar)
# print(l.count(7))

# print(l)
# print(max(l))
# print(l.index(max(l)))


# for i in range(0, len(l)):
#     if i%2 == 1:
#         print(l[i], end=" ")


# t_kotta = 0
# for i in l:
#     if i > 40000:
#         t_kotta += 1
# print(f"{t_kotta} ta mavjud.")



#
#
# ismlar = ["Ali", "Vali", "Ahmad", "Zebo", "Tursunboy", "Toshmatjon", "Ahadquli",
#           "Holmat", "Teshmat", "Eshmat", "Samir", "Zarifjon"]
# print(ismlar)
#
# while True:
#     ism = input("Ism kiriting: ")
#     if ism in ismlar:
#         print("bu ism mavjud")
#     else:
#         print("Ism qo'shildi!")
#         ismlar.insert(0, ism)
#
#     if ism == "stop" or ism == "STOP":
#         break
#     print(ismlar)
#
# print(ismlar)
#





a = int(input("Son kiriting: "))

for i in range(1, a+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ", end=" ")
    elif i % 3 == 0:
        print("FIZZ", end=" ")
    elif i % 5 == 0:
        print("BUZZ", end=" ")
    else:
        print(i, end=" ")













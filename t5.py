a = int(input("Введите количество студентов:"))
b = int(input("Введите количество студентов:"))
c = int(input("Введите количество студентов:"))
if a % 2 ==0:
    class_1 = a // 2
elif a % 2 == 1:
    class_1 = a // 2 + 1

if b % 2 == 0:
    class_2 = b // 2
elif b % 2 == 1:
    class_2 = b // 2 + 1
if  c % 2 == 0:
    class_3 = c // 2
elif c % 2 == 1:
    class_3 = c // 2 + 1
print(class_1 + class_2 + class_3)
    
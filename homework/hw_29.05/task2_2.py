n = int(input("Введите число "))

flag = True
i = 1

while flag:
    if i ** 2 <= n:
        print(i ** 2)
    else:
        flag = False
    i += 1


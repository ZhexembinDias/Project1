n = int(input("Количество карт "))
num_list = []

for i in range(0, n-1):
    a = int(input("Введите число "))
    num_list.append(a)

for i in range(1, n+1):
    if i not in num_list:
        print(i)



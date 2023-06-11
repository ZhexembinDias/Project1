tuple_1 = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
fruit_name = input("Введите название фрукта ")

j = 0

for elem in tuple_1:
    if fruit_name in elem:
        j += 1

print(j)
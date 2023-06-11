my_list = [1, 2, 3]

try:
    index = 2
    value = my_list[index]
    print(value)
except IndexError:
    print("Ошибка доступа к элементу списка")
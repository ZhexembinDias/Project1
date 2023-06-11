# написать функцию, которая принимает массив имён и “искомое имя”. Возвращает True если имя есть в массиве.

name_list = ["Bogdan", "Roman", "Evgenii", "Dias"]

def search_name(list_names, target_name):
    if target_name in name_list:
        return True
    else:
        return False


list_n = ["Богдан", "Евгений", "Диас"]
t_name = "Диас"
result = search_name(list_n, t_name)
print(result)
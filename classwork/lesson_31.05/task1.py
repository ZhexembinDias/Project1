# написать функцию, которая принимает 3 массива с числами и возвращает их в одном массиве,
# но отсортированным в порядке возврастая по сумме их “начинки”.

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
arr3 = [4, 6, 2, 7, 1]

def my_sort(a, b, c, is_reversed: bool):
    #попытка отсортировать внаглую
    res = [a, b, c]
    print(res)

    sum_a = sum(a)
    sum_b = sum(b)
    sum_c = sum(c)

    #создание пар (массив, сумма)
    #сортировка по ключу
    tuple_res = sorted(((a, sum_a), (b, sum_b), (c, sum_c)), key= lambda x:x[1], reverse = is_reversed)
    print(tuple_res)

    #пересобераем в массив
    res = []
    for i in tuple_res:
        res.append(i[0])
    print(res)

    return res



res = my_sort(arr3, arr2, arr1, False)
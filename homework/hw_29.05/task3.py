#2.	Реализуйте рекурсией проверку на совпадение всех элементов массива с числами.

def task(n, num_list):
    if n not in num_list:
        print(n)
    if n == 1:
        return 1
    else:
        return task(n - 1, num_list)

num_list1 = [2, 3, 4, 5, 6]
n = 6

task(6, num_list1)

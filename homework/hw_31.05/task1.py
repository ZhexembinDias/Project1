def plus_two(number):
    try:
        return number + 2
    except TypeError:
        print("Произошла ошибка типа данных")

print(plus_two(2))
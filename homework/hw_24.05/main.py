s = float(input("Стоимость подписки "))
p = float(input("Стоимость пиццы "))
m = float(input("Зарплата "))

if m >= p + s:
    print("Да")
else:
    print("Нет")
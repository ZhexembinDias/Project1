a = float(input("Введите число а "))
b = float(input("Введите число b "))
c = input("Введите действие ")

if c == "+":
    print(f"{a} + {b} = {a + b}")
elif c == "-":
    print(f"{a} - {b} = {a - b}")
elif c == "*":
    print(f"{a} * {b} = {a * b}")
elif c == "/":
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print(f"{a} / {b} = {a / b}")
else:
    print(f"Введите правильное действие, {c} не правильно")

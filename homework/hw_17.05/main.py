# Задание 1
# login = input("Введите логин\n")
# password = input("Введите пароль\n")

# if login == "user" and password == "qwerty":
#    print(f"{login}  {password}\nAuthentication completed")
# else:
#    print("Invalid login or password")

# if login != "user":
#    print("Invalid login")
# elif password != "qwerty":
#    print("Invalid password")
# else:
#    print("Authentication completed")

# Задание 2

dict_kurs = {
    "USD": 420,
    "EUR": 510,
    "RUB": 5.8
}

sum_tg = int(input("Введите сумму "))
print("Choose currency:\n[1] USD \n[2] EUR \n[3] RUB\n")
num_kurs = int(input("Выберите валюту "))

if num_kurs == 1:
    print(f"{sum_tg/dict_kurs['USD']} USD")
elif num_kurs == 2:
    print(f"{sum_tg /dict_kurs['EUR']} EUR")
elif num_kurs == 3:
    print(f"{sum_tg / dict_kurs['RUB']} RUB")
else:
    print("Введите число от 1 до 3")

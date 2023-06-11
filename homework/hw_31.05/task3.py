import requests
import json

a = int(input("Введите ID "))


# Отправка GET-запроса
response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{a}")

# Проверка статуса ответа
if response.status_code == 200:
    print("Запрос выполнен успешно")
else:
    print("Произошла ошибка при выполнении запроса")

res_dict = response.json()

# Открываем файл для записи
file_path = f"{a}_id.json"
with open(file_path, "w") as file:
    # Записываем данные в файл в формате JSON
    json.dump(res_dict, file)

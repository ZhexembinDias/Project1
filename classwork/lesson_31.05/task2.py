#json -> txt
#прочитать json
#записать в txt

import json

with open("temp/new.json", mode= "r", encoding="utf-8") as json_file:
    # todo конвертация json файла в питоновский словарь (list)
    dictionaries = json.load(json_file)

print(dictionaries)
print(type(dictionaries))      # <class 'list'>
print(type(dictionaries[0]))   # <class 'dict'>

# todo откртытие txt файла на запись с помощью контекстного менеджера
with open("temp/new.json", mode= "r", encoding="utf-8") as txt_file:
    # todo перебор всех словарей и запись данных из каждого на новую строку в txt файл
    for dictionary in dictionaries:
        new_string = f"{dictionary['userID']} | {dictionary['id']} | {dictionary['title']} | {dictionary['completed']} \n"
        txt_file.write(new_string)


# with open("temp/new.json", mode= "r", encoding="utf-8") as json_file:
#     with open("temp/new.json", mode="r", encoding="utf-8") as txt_file:
#         for dictionary in dictionaries:
#             txt_file.write(f"{dictionary['userID']} | {dictionary['id']} | {dictionary['title']} | {dictionary['completed']} \n")
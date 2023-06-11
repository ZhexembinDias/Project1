dict1 = {
    "Привет": "Hello",
    "Собака": "Dog",
    "Кошка": "Cat"
}

class Dictionary:
    def append_elem(self, word, perevod):
        dict1[word] = perevod

    def delete_elem(self, word):
        if word in dict1:
            dict1.pop(word)
        else:
            print("Такого слово не существует")

    def search_elem(self, word):
        perevod = dict1.get(word, "")
        if perevod == "":
            print("В словаре нет такого перевода")
        else:
            return perevod

    def rename_elem(self, word, perevod):
        dict1[word] = perevod


obj = Dictionary()

obj.append_elem("яблоко", "apple")
print(dict1)
obj.delete_elem("Кошка")
print(dict1)
print(obj.search_elem("Привет"))
obj.rename_elem("Собака", "Dog1")
print(dict1)

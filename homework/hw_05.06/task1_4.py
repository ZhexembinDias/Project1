tuple_1 = ("banana", "apple", "strawberry","banana", "apple", "strawberry","banana", "apple", "strawberry")
list1 = []
fruit_name = input("Введиет название фрукта ")
zamena = input("Замена ")


for elem in tuple_1:
    if fruit_name == elem:
        list1.append(zamena)
    else:
        list1.append(elem)

print(list1)

tuple_1_new = tuple(list1)

print(tuple_1_new)

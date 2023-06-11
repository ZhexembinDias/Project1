tuple_1 = ("banana", "apple", "strawberry","banana", "apple", "strawberry","banana", "apple", "strawberry")
fruit_name = input("Введиет название фрукта ")

j = 0

for elem in tuple_1:
    if fruit_name == elem:
        j += 1

print(j)    

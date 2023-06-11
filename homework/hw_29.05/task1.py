a = int(input("Число игроков команды А "))
b = int(input("Число игроков команды B "))

flag = True
i = 1

while flag:

    if i % a == 0 and i % b == 0:
        flag = False
    else:
        # i = i + 1
        i += 1

print(i)

str1 = "abba"
a = int(input("Введите число "))

str1_new = ""

for i in str1:
    unicode = ord(i)
    letter = chr(unicode + a)
    str1_new += letter


print(str1_new)
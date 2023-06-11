# В папке выше текущей (если нет папки, создать)
# дописать в текстовый файл(если нет файла, создать)
# надпись 'Python is awesome'
import os.path

top_path = "../temp"

if not os.path.exists(top_path):
    os.mkdir(top_path)

with open(f"{top_path}/temp.txt", mode="a", encoding="utf-8")as file:
    file.write(txt + "\n")


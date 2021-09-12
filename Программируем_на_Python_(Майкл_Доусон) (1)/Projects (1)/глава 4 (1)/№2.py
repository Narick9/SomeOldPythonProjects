# Задача из главы 5

print("Введите текст, а программа выведет его наоборот.")

text = input()
new_text = ""

while text:
    new_text += text[-1]
    text = text[:-1]

print("У нас получилось: ", new_text)

input("Для выхода нажмите Enter.")

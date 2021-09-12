from collections import OrderedDict

gloss = OrderedDict()

gloss["словарь"] = "список объектов вида ключ-значение"
gloss["if-elif-else"] = "операторы условий"
gloss["список"] = "набор объектов"
gloss["кортеж"] = "неизменяемый набор объектов"
gloss["python"] = "язык программирования"

gloss["set"] = "множество неповторяющихся объектов"
gloss["print"] = "функция вывода строки в терминал"
gloss["for"] = "цикл, созданный для работы с массивами данных"
gloss["="] = "оператор присваивания"
gloss["=="] = "логическое выражение, проверяющее полное сходство"

for key, item in gloss.items():
    print(key.title() + " - " + item)

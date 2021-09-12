# Мой вариант ответа анаграммы из учебника

import random

WORDS = ("привет", "муся", "стена", "дом", "квартира")

word = random.choice(WORDS)
CONST = word
n = 0
new_word = ""
ans = ""

while word:
    n = random.randrange(len(word))
    new_word += word[n]
    word = word[:n] + word[n + 1:]

print(new_word)
    
while True:
    print("Ваш вариант ответа: ", end = " ")
    ans = input()
    if ans == CONST:
        break
    print("Вы не угадали, попробуйте снова.\n")

print("Это правельный ответ!\n")

input("Для выхода нажмите Enter")

# Задача из главы 5

import random

WORDS = ["Дом", "Муся", "Кваритара", "Тося"]

used = []
i = 0
n = 0

while i < len(WORDS):
    i += 1
    n = random.randrange(len(WORDS))
    if n in used:
        i -= 1
        continue
    print(WORDS[n], end = " ")
    used.append(n)

input("\nЧтобы продолжить нажмите Enter.")
        
while WORDS:
    print(WORDS.pop(random.randrange(len(WORDS))))


    

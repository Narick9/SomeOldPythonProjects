# Игра в кости

import random

n1 = random.randint(1, 6)
n2 = random.randint(1, 6)
total = n1 + n2

print("Кубики выбили", n1, "и", n2, "в сумме выходит", total)

input("Для выхода нажмите Enter")

# Симулятор пирожка с "сюрпризом"

import random

secret = random.randint(1, 5)

print("Симулятор пирожка с \"сюрпризом\"")
print("Вам попался пирожок с...")

if secret == 1:
    print("Картошкой!")
elif secret == 2:
    print("Капустой и мясом!")
elif secret == 3:
    print("Яйцом и зелёным луком!")
elif secret == 4:
    print("Яблоком!")
elif secret == 5:
    print("Целым рагу!")

input("Для выхода нажмите Enter.")




# Симулятор броска монетки

import random

print("Симулятор броска монетки")

score = 0
n1 = 0
n2 = 0

while score < 100:
    r = random.randint(1, 2)
    if (r == 1):
        n1 += 1
    else:
        n2 += 1
    score += 1

print("Вам выпало...", n1, "орлов и...", n2, "решок!")
        
input("Чтобы продолжить нажмите Enter.") 

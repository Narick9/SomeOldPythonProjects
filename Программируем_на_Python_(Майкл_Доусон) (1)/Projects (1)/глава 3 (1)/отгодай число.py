# Игра "Отгодай число"
# Написана мной по псевдокоду

import random

print('\t"Отгодай число"')
print("\nПравила игры:")
print("Попробуйте отгодать число от 1 до 100")
print("с подсказками компьютера!\n\n")

secret = random.randint(1, 100)
answer = 0
try_n = 1

while True:
    print("Попытка номер", try_n)
    while not answer:
        answer = int(input("Ваш вариант ответа: "))
    if answer == secret:
        print("Ухты! Вы отгодали с", try_n, "попытки!")
        break
    else:
        if answer < secret:
            print("Ваше число меньше.")
        else:
            print("Ваше число больше.")
        print("\n")
        try_n += 1
        answer = 0

input("\n\nДля завершения нажмите Enter")
    

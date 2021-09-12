# Игра "Отгодай число"
# Написана мной по псевдокоду

import random

print('\t"Отгодай число"')
print("\nПравила игры:")
print("Попробуйте отгодать число от 1 до 100")
print("с подсказками компьютера!")
print("У вас всего 7 попыток!")

secret = random.randint(1, 100)
answer = 0
try_n = 1

while True:
    print("\n")
    if try_n >= 7:
        print("У вас кончились попытки!")
        break
    print("Попытка номер", try_n)
    while not answer:
        answer = int(input("Ваш вариант ответа: "))
    if answer == secret:
        print("\n")
        print("Ухты! Вы отгодали с", try_n, "попытки!")
        break
    else:
        if answer < secret:
            print("Ваше число меньше.")
        else:
            print("Ваше число больше.")
        try_n += 1
        answer = 0

input("\n\nДля завершения нажмите Enter")
    

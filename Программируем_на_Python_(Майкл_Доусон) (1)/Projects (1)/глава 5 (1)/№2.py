# Задача из главы 5

print(
"""
\"Генератор персонажей\"
Вы можете распределить свои очки жизни
на характеристики своего персонажа.
""")

powers = (["Сила", 0], ["Здоровье", 0], ["Мудрость", 0], ["Ловкость", 0])

pool = 30
choice = None

while choice != 1:
    print("\n")
    
    print("Ваши показатели:", powers)
    print("Вам доступно", pool, "очков жизни.", end = " ")
    print(
"""
Меню действий:
1 - Выйти;
2 - Улучшить характеристики;
3 - Вернуть очки жизни
""")
    choice = int(input("Выбор: "))
    
    if choice == 1:
        break
    
    elif choice == 2 or choice == 3:
        print(
"""
Выберите характеристику:
1 - Сила;
2 - Здоровье;
3 - Мудрость;
4 - Ловкость;
""")
        char = int(input("Выбор: "))
        if not (char >= 1 and char <= 4):
            print("Такого пункта нет в меню.")
            continue

        n = int(input("Количество очков жизни: "))
        if choice == 2:
            if not (n >= 0 and n <= pool):
                print("У вас нет стольки очков жизни.")
                continue
            pool -= n
            powers[char - 1][1] += n
            
        elif choice == 3:
            if not (n <= powers[char - 1][1] and n >= 0):
                print("Вы не можете возвратить столько очков жизни.")
                continue
            pool += n
            powers[char - 1][1] -= n
            
    else:
        print("В меню нет такого пункта.")

        
input("\nЧтобы продолжить нажмите Enter.")

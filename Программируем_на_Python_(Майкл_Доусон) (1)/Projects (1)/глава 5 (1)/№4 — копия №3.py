# Задача из главы 5

families = {"Артур": ["Камиль", ""],
            "Генри": ["Уильям", ""],
            "Джон": ["Уильям", ""],
            "Томас": ["Самуэль-младший", ""],
            "Исла": ["Питер", "Марк"],
            "Дьюк": ["Дьюк", "Джордж VI"]}

print(
"""
\"Кто твой папа?\"
""")

choice = None

while choice != 0:
    input("Для продолжения нажмите Enter")
    print("\n")
    print(
"""
    Меню выбора:
0 - Выйти;
1 - Вывести весь список;
2 - Узнать предков по имени;
3 - Добавить личность;
4 - Добавить правку;
5 - Удалить человека.
""")
    choice = int(input("Выбор: "))
    
    if choice == 0:
        break
    
    elif choice == 1:
        print("Имя:\t\t\tОтец:\t\t\tДед:")
        for name in families:
            print(name, "\t\t\t", families[name][0], "\t\t\t", families[name][1])

    elif choice == 2:
        name = input("Введите имя личности: ")
        name = name.title()
        print("Имя:\t\t\tОтец:\t\t\tДед:")
        print(name, "\t\t\t", families[name][0], "\t\t\t", families[name][1])

    elif choice == 3:
        name = input("Введите имя личности: ")
        name = name.title()
        if name in families:
            print("Имя уже есть в базе")
            continue
        sec_name = input("Введите имя отца: ")
        th_name = input("Введите имя деда: ")
        families[name][0] = sec_name
        families[name][0] = th_name

    elif choice == 4:
        name = input("Введите имя личности: ")
        name = name.title()
        if name not in families:
            print("Нат данных")
            continue
        sec_name = input("Введите поправку отца: ")
        th_name = input("Введите правку деда: ")
        families[name][0] = sec_name
        families[name][1] = th_name

    elif choice == 5:
        name = input("Введите имя личности: ")
        name = name.title()
        if name not in families:
            print("Нет данных")
            continue
        del families[name]
            
input("\nДля продолжения нажмите Enter")

magicans = ["Гарри Гудини", "Дай Вернон", "Ури Геллер"]

def show_magicans(magicans):
    """Выводит имя каждого фокусника в списке"""
    for magican in magicans:
        print(magican.title())

def make_great(sp):
    """Добавляет приставку great к каждому элементу списка"""
    i = 0
    while i < len(sp):
        sp[i] = "Great " + sp[i]
        i += 1
    return sp

great_magicans = make_great(magicans[:])

for sp in (great_magicans, magicans):
    print("Великие фокусники:")
    show_magicans(sp)
    print()

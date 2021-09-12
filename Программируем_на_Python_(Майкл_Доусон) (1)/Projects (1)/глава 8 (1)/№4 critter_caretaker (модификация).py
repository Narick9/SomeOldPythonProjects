# Critter Caretaker
# A virtual pet to care for
# Модифицированна по условию задачи из главы 8

#Добавленная часть
import random

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

# Добавленная часть
# Количество зверушек
qty_critters = 3

# Модифицированная функция
def main():
    crits = []
    
    for i in range(qty_critters):
        print("What do you want to name your critter", i, "?: ", end = "")
        crit_name = input()
        crits.append(Critter(crit_name,
                    random.randrange(1, 4), random.randrange(1, 4)))

    choice = None  
    while choice != "0":
        print \
        ("""
        Зооферма
    
        0 - Quit
        1 - Прослушать всех зверюшек
        2 - Покормить всех зверюшек
        3 - Поиграть со всеми зверюшками
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # Прослушка всех зверюшек
        elif choice == "1":
            for crit in crits:
                crit.talk()

        # Кормление всех зверюшек
        elif choice == "2":
            for crit in crits:
                crit.eat()

        # Играние со всеми зверюшками
        elif choice == "3":
            for crit in crits:
                crit.play()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")


main()
("\n\nPress the enter key to exit.") 

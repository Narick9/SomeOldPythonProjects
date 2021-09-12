# По условию задачи №4 из главы 9

import random

class World(object):
    TERRAIN = [["водопад", "возывшенность", "джунгли", "побережье"],
               ["возвышенность","болото","джунгли","побережье"],
               ["джунгли","джунгли","побережье","остров"],
               ["джунгли","возвышенность","река","устье реки"]]
    TIME = ["утро", "полдень", "вечер", "ночь"]
    WEATHER = ["чистое небо", "облачно", "сильный ливень",
               "ветер"]
    
    def __init__(self, time = 0):
        #определение территории по карте
        self.terrain_y = random.randrange(len(World.TERRAIN))
        self.terrain_x = random.randrange(len(World.TERRAIN[self.terrain_y]))
        self.terrain = World.TERRAIN[self.terrain_y][self.terrain_x]
        #выбор времени
        self.time = World.TIME[time]
        #выбор погоды
        self.weather = random.choice(World.WEATHER)

    def __str__(self):
        rep = "\n\tТип местности: " + str(self.terrain) \
        + "\n\tВремя суток: " + str(self.time) \
        + "\n\tПогода на данный момент: " + str(self.weather)
        return rep

    def new_location(self, x, y):
        if y in range(len(World.TERRAIN)) and x in range(len(World.TERRAIN[0])):
            self.terrain = World.TERRAIN[y][x]
            self.terrain_y = y
            self.terrain_x = x
            return True
        else:
            print("Вы не можете попасть сюда из-за океана, реки или обрыва.")
            return False

    def get_location(self):
        return [self.terrain_x, self.terrain_y]
    
    def next_time(self):
        #следующее время дня
        if World.TIME.index(self.time) + 1 >= len(World.TIME):
            self.time = World.TIME[0]
        else:
            self.time = World.TIME[World.TIME.index(self.time) + 1]
        if self.time == "утро":
            self.next_weather()

    def next_weather(self):
        #смена погоды
        self.weather = random.choice(World.WEATHER)

class Explorer(object):
    DAYS_TO_HELP = 15
    
    def __init__(self, food = 7):
        self.location = World()
        self.food = food
        self.days_alive = 1

    def __str__(self):
        rep = "Описание положения:" \
        + "\t" + str(self.location) \
        + "\n\tЕды на дней: "
        if self.food < 0:
            rep += str(0)
        else:
            rep += str(self.food)
        rep += "\n\tДень: " + str(self.days_alive)
        if self.food < 0:
            rep += "\n\tУ вас голод!"
        return rep

    #передвежение
    def next_location(self, choice = ""):
        #выбор и проверка новой локации
        y = self.location.terrain_y
        x = self.location.terrain_x
        if choice == "w":
            y -= 1
        elif choice == "a":
            x -= 1
        elif choice == "s":
            y += 1
        elif choice == "d":
            x += 1
        else:
            print("Неверное направление пути.")
        # изменение показателей
        if self.location.new_location(x, y):
            self.next_time()

    #смена времени дня
    def next_time(self):
        self.location.next_time()
        if self.location.time == "ночь":
            self.food -= 1
            self.days_alive += 1
            print("Вы устроили ночлег или легли спать.")
            self.next_time()

    #случайное получение еды
    def take_food(self):
        if self.location.terrain in ("река", "устье реки", "побережье"):
            if not random.randrange(6):
                print("Вам удалось поймать немного рыбы.")
                self.food += 2
        if self.location.terrain in ("джунгли"):
            if not random.randrange(5):
                self.food += 1
                print("Вам удалось найти немного спелых фруктов.")
    
    #   Функции для возврата значений
        
    def is_enough_food(self):
        return self.food > -3 #меньше 3 дней без еды

    def is_save_day(self):
        return self.days_alive >= Explorer.DAYS_TO_HELP
        

    #   Функции пояснения для игрока
    
    def print_menu(self):
        print(
"""
    Меню игры:
        w - двигаться вперёд;
        a - двигаться влево;
        s - двигаться назад;
        d - двигаться вправо;
        выйти - выход из игры;
""")

    def print_prolog(self):
        print(
"""
    Вы очнулись в потерпевшем крушение самолёте где-то у побережья Южной Америки.
    Вы единственный выживший. У вас есть еда и вода на ближайшую неделю.
    Вам предстоит изучить местность, чтобы найти еды, и дождаться спасателей.
""")

    def print_save(self):
        print(
"""
    Вы просыпаетесь от звука крутящихся лопастей вертолёта. Незамедлительно
    достаёте из потрёпанного рюкзака сигнальный пистолет и заряжаете его
    припасёнными сигнальными ракетами. Вы стреляете вверх и надетесь, что
    её заметят. Шум вертолёта усиливается. С него, по верёвочной лестнице,
    спускаются спасатели и поднимают вас в вертолёт. Вы выжили!
""")

    def print_death(self):
        print(
"""
    Измученные от голода, вы не просыпаетесь этим утром. Шансы, что найдут
    ваше тело очень низки.
    В утренних новостях говорится, что в джунглях Южной Америки найден
    пропавший самолёт. Никто из пассажиров не выжил.
""")



#основная часть
def main():
    print(
"""
        Добро пожаловать в \"Исследователь\"!
    Сможете ли вы выжить в этом удивительном мире?

""")
    player = Explorer()
    player.print_prolog()
    player.print_menu()

    print("---------------------")
    
    ans = None
    while ans != "выйти":
        print(player)
        print()
        print(player.location.get_location())
        ans = input("Ваш выбор: ").lower()

        if ans == "выйти":
            continue
        elif ans in ("w", "a", "s", "d"):
            player.next_location(ans)
            
            if player.is_save_day():
                player.print_save()
                break

            if not player.is_enough_food():
                player.print_death()
                break

            print("Вы отправились в путь.")
            player.take_food()
        else:
            print("В меню нет этого пункта.")
        
        print()
            

#начало программы
#try:
main()
#except:
    #print("Неизвестная ошибка.")

input("Для продолжения нажмите Enter...")

# По условию задачи из главы 8

class tv(object):
    """Виртуальный телевизор"""
    #конструктор
    def __init__(self, n_channel = 1, n_volume = 10):
        print("У вас появился телевизор!")
        self.__channel = n_channel
        self.__volume = n_volume

    @property
    def channel(self):
        return self.__channel
    
    @channel.setter
    def channel(self, n_channel):
        if n_channel in range(1, 71):
            self.__channel = n_channel
            print("Переключаю на канал под номером ", n_channel)
        else:
            print("Недопустимый номер канала.")

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, n_volume):
        if n_volume in range(0, 101):
            self.__volume = n_volume
            print("Уровень громкости успешно изменён.")
        else:
            print("Уровень звука должен быть в пределах от 0 до 100")

    def print_settings(self):
        print("Канал:", self.channel)
        print("Уровень звука:", self.volume)


def main():
    user_tv = tv()
    
    change = ""
    while change != "0":
        user_tv.print_settings()
        print(
"""
    Меню телевизора:
    
0 - Выйти;
1 - Сменить канал;
2 - Изменить уровень громкости;

""")
        change = input("Выбор: ")

        if change == "0":
            print("Выход...")
        elif change == "1":
            n_channel = int(input("Номер канала: "))
            user_tv.channel = n_channel
        elif change == "2":
            n_volume = int(input("Уровень громкости: "))
            user_tv.volume = n_volume
        else:
            print("Неверный выбор меню.")

        print("\n----------------\n")

        
    
main()
input("Для продолжения нажмите Enter.")

# По условию задачи №2 главы 9

import cards_mod, games_mod, random

class War_Player(object):
    """Игрок для игры в войну (карта с именем)"""
    def __init__(self, name):
        self.name = name
        self.rank = None
        self.suit = None

    def add(self, card):
        #получает карту и сохраняет её
        self.rank = card.rank
        self.suit = card.suit
        
    @property
    def score(self):
        #Счёт равен номиналу полученной карты
        s = 0
        if self.rank:
            s = cards_mod.Card.RANKS.index(self.rank) + 1
        return s

    def __str__(self):
        rep = self.name + ":\t" + self.rank + self.suit \
                + "\t" + "(" + str(self.score) + ")"
        return rep

    def get_name(self):
        return self.name

def play_war(names):
    """Игра в войну"""
    #ввод имён
    players = []
    for name in names:
        player = War_Player(name)
        players.append(player)

    deck = cards_mod.Deck()
    deck.populate()
    deck.shuffle()

    #вытягавание карт по очереди
    deck.deal(players, per_hand = 1)
    
    #вывод результатов и определение победителя
    print("Имя:\tКарта:\tСчёт:")
    win_player = War_Player("winner") #"winner" - просто заполнитель
    for player in players:
        print(player)
        if player.score > win_player.score:
            win_player = player

    #вовод победителя
    print(win_player.get_name(), "побеждает!")

# Основная часть

def main():
    print(
"""
        Добро пожаловать в Войну!
""")
    n = games_mod.ask_number("Сколько игроков учавствует (2 - 5): ",
                                 low = 2, high = 6)
    names = []
    for _ in range(n):
        name = input("Введите имя игрока: ")
        names.append(name)
    print()

    again = "y"
    while again == "y":
        play_war(names)
        print()
        again = games_mod.ask_yes_no("Хотите продолжить?: ")

try:
    main()
except:
    print("Неизвестная ошибка.")

input("Для продолжения нажмите Enter...")

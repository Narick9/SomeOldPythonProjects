# Blackjack
# From 1 to 7 players compete against a dealer
# Модифицированна по условию задачи №1 из главы 9
# Модифицированна по условию задачи №3 из главы 9

import cards_mod, games_mod     

# Модифицированный класс
class BJ_Card(cards_mod.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

# Модифицированный класс
class BJ_Deck(cards_mod.Deck):
    """ A Blackjack Deck. """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
    
# Модифированный класс
class BJ_Hand(cards_mod.Hand):
    """ A Blackjack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
        if self.total:
            rep += "(" + str(self.total) + ")"        
        return rep

    @property     
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
        
        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
              t += card.value

        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
                
        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10   
                
        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """ A Blackjack Player. """
    START_CAPITAL = 2000
    
    def __init__(self, name, bet = 0):
        super().__init__(name)
        self.bet = bet
        self.capital = BJ_Player.START_CAPITAL

    def __str__(self):
        rep = self.name + "($" + str(self.capital) + "):\t" \
                + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"        
        return rep

    def is_hitting(self):
        response = games_mod.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def is_enough(self):
        return self.capital >= self.bet

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")
        print(self.name, "проиграл", self.bet, "долларов.")
        self.capital -= self.bet

    def win(self):
        print(self.name, "wins.")
        print(self.name, "выиграл", self.bet, "долларов.")
        self.capital += self.bet

    def push(self):
        print(self.name, "pushes.")

    def not_enough(self):
        print(self.name, "обанкротился.")

        
class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

    def is_enough(self):
        return True


class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names, bets):      
        self.players = []
        for i in range(len(names)):
            player = BJ_Player(names[i], bets[i])
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting() and player.is_enough():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()
            if not player.is_enough():
                player.not_enough()
                self.players.remove(player)
           
    def play(self):
        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # reveal dealer's first 

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()                    
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()
        
# Модифицированная функция
def main():
    print("\t\tWelcome to Blackjack!\n")
    
    names = []
    bets = []
    number = games_mod.ask_number("How many players? (1 - 7): ",
                low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
        bet = games_mod.ask_number("Ваша ставка (1$ - 1000$): ",
                low = 1, high = 1001)
        bets.append(bet)
    print()
        
    game = BJ_Game(names, bets)

    again = None
    while again != "n":
        game.play()
        if game.players:
            again = games_mod.ask_yes_no("\nDo you want to play again?: ")
        else:
            print("Игроков не осталось.")
            break


try:
    main()
except:
    print("Неизвестная ошибка.")

input("\n\nPress the enter key to exit.")




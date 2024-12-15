from Game_Cards.DeckOfCards import DeckOfCards
from Game_Cards.Player import Player

class CardGame:
    def __init__(self, player_one_name, player_two_name, cards_number = 26):
        if len(player_one_name) < 1 or len(player_two_name) < 1:
            raise ValueError("Player name can't be empty.")
        if type(player_one_name) != str or type(player_two_name) != str:
            raise TypeError("Player name must be a string.")
        if type(cards_number) != int:
            raise TypeError("Cards number must be an int.")
        if cards_number < 10 or cards_number > 26:
            cards_number = 26
        self.player_one = Player(player_one_name, cards_number)
        self.player_two = Player(player_two_name, cards_number)
        self.game_cards_deck = DeckOfCards()
        self.start_game = True
        self.new_game()
        self.start_game = False

    def new_game(self):
        if self.start_game:
            self.game_cards_deck.cards_shuffle()
            self.player_one.set_hand(self.game_cards_deck)
            self.player_two.set_hand(self.game_cards_deck)
        else:
            print("Game can be started from init only")

    def get_winner(self):
        if len(self.player_one.player_cards) > len(self.player_two.player_cards):
            return self.player_one
        elif len(self.player_one.player_cards) < len(self.player_two.player_cards):
            return self.player_two
        else:
            return None

if __name__ == "__main__":
    My_Game = CardGame("Raz", "Dom", 10)
    print(My_Game.player_one)
    print(My_Game.player_two)
    print(My_Game.game_cards_deck)
    print(My_Game.get_winner())
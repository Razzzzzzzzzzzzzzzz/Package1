from Game_Cards.DeckOfCards import DeckOfCards
from Game_Cards.Player import Player

class CardGame:
    def __init__(self, player_one_name, player_two_name, cards_number = 26):
        if type(player_one_name) != str or type(player_two_name) != str:
            raise TypeError("Player name must be a string.")
        MIN_NAME_LENGTH = 1
        if (len(player_one_name) < MIN_NAME_LENGTH or
                len(player_two_name) < MIN_NAME_LENGTH):
            raise ValueError("Player name can't be empty.")
        if type(cards_number) != int:
            raise TypeError("Cards number must be an int.")
        MIN_CARDS = 10
        MAX_CARDS = 26
        if cards_number < MIN_CARDS or cards_number > MAX_CARDS:
            cards_number = MAX_CARDS # Default value
        self.player_one = Player(player_one_name, cards_number)
        self.player_two = Player(player_two_name, cards_number)
        self.game_cards_deck = DeckOfCards()
        self.start_game = True # Informing new_game that it started from init
        self.new_game()
        self.start_game = False # so new_game won't work if called out of init

    def new_game(self):
        """provides both players a shuffled cards deck"""
        if self.start_game: # If method has been called from _init_
            self.game_cards_deck.cards_shuffle()
            self.player_one.set_hand(self.game_cards_deck)
            self.player_two.set_hand(self.game_cards_deck)
        else:
            print("Game can be started from init only")

    def get_winner(self):
        """Returns the winning player who has the most cards,
         or none if no one won."""
        if (len(self.player_one.player_cards) >
                len(self.player_two.player_cards)):
            return self.player_one
        elif (len(self.player_one.player_cards) <
              len(self.player_two.player_cards)):
            return self.player_two
        else:
            return None
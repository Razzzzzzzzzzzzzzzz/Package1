from Game_Cards.Card import Card
from Game_Cards.DeckOfCards import DeckOfCards
from random import randint

class Player:
    def __init__(self, name, cards_number = 26):
        if len(name) < 1:
            raise ValueError("Name can't be empty")
        if type(name) != str:
            raise TypeError("name must be a string!")
        self.name = name
        if 10 <= cards_number <= 26:
            self.cards_number = cards_number
        else:
            self.cards_number = 26
        self.player_cards = []

    def __str__(self):
        return f"-----[{self.name} - {len(self.player_cards)} Cards]-----\n{self.player_cards}"

    def set_hand(self, cards_deck = DeckOfCards()):
        if type(cards_deck) != DeckOfCards:
            raise TypeError("Cards Deck must be a DeckOfCards Type!")
        if len(cards_deck.cards) > 0:
            for cards in range(self.cards_number):
                self.player_cards.append(cards_deck.deal_one())

    def get_card(self):
        if len(self.player_cards) > 0:
            return self.player_cards.pop(randint(0, len(self.player_cards) - 1))

    def add_card(self, new_card):
        if type(new_card) == Card:
            self.player_cards.append(new_card)

if __name__ == "__main__":
    player1 = Player("Raz", 10)
    game_cards = DeckOfCards()
    print(game_cards)
    player1.set_hand(game_cards)
    print(game_cards)
    print(player1.player_cards)
    print("GAME CARDS")
    print(player1.get_card())
    print(player1.get_card())
    print(player1.get_card())
    print(player1.player_cards)
    player1.add_card(game_cards.deal_one())
    print(player1.player_cards)
    print(game_cards)
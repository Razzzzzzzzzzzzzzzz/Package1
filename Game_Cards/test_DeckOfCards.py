from unittest import TestCase
from Game_Cards.Card import Card
from Game_Cards.DeckOfCards import DeckOfCards

class TestDeckOfCards(TestCase):

    def setUp(self):
        self.my_cards_deck = DeckOfCards()

    def test_init_valid_deck_length(self):
        """Checks if the init creates a full cards deck of 52 cards."""
        self.assertEqual(52, len(self.my_cards_deck.cards))

    def test_init_valid_type(self):
        """Checks if the type of the cards deck is a list"""
        self.assertEqual(type(self.my_cards_deck.cards), list)

    def test_init_valid_value_range(self):
        """Checks if the range of the cards value is within the range"""
        valid_cards_value_range = True
        for card in self.my_cards_deck.cards:
            if card.value < 2 or card.value > 14:
                valid_cards_value_range = False
        self.assertTrue(valid_cards_value_range)

    def test_init_valid_symbol_range(self):
        """Checks if the range of the cards symbol is within the range"""
        valid_cards_symbol_range = True
        for card in self.my_cards_deck.cards:
            if card.symbol < 1 or card.symbol > 4:
                valid_cards_range = False
        self.assertTrue(valid_cards_symbol_range)

    def test_init_valid_no_duplicates(self):
        """Testing for identical cards in the cards deck"""
        no_duplicates = True
        for card1 in range(52): # The entire cards deck
            for card2 in range(card1 + 1,52): # The cards forward from
                                              # the current card.
                if card1 == card2: # If a card is found identical to
                                   # another card in the deck
                    no_duplicates = False # shuffle method worked if the
                                          # line above is true
        self.assertTrue(no_duplicates)

    def test_valid_shuffle(self):
        """Testing if an un-shuffled deck of cards is equal to a
        shuffled deck of cards. If all cards are equal, then the
        test will fail"""
        shuffled_cards_deck = DeckOfCards()
        shuffled_cards_deck.cards_shuffle()
        shuffled = False # Will be true if the cards deck is shuffled.
        for i in range(52):
            if shuffled_cards_deck.cards[i] != self.my_cards_deck.cards[i]:
                shuffled = True # If two cards on the same index are different,
                                # the cards deck is shuffled.
                break
        self.assertTrue(shuffled)

    def test_invalid_shuffle_empty(self):
        """Testing if the method works when attempting to shuffle
        an empty list."""
        self.my_cards_deck.cards = []
        self.my_cards_deck.cards_shuffle()
        self.assertEqual(self.my_cards_deck.cards, [])

    def test_deal_one_valid_remove_one_card(self):
        """Testing for 1 card to be removed from the cards deck."""
        dealt_cards_deck = self.my_cards_deck.cards.copy()
        self.my_cards_deck.deal_one() # Removes a card from the cards deck
        self.assertEqual(len(dealt_cards_deck) - 1,
                         len(self.my_cards_deck.cards))

    def test_deal_one_valid_return_card(self):
        """Testing if the returned object is a card."""
        returned_card = self.my_cards_deck.deal_one()
        self.assertEqual(type(returned_card), Card)

    def test_deal_one_invalid_empty_cards_deck(self):
        """Testing the deal one method to not do anything when
        there are no cards"""
        self.my_cards_deck.cards = []
        other_cards_deck = self.my_cards_deck.cards.copy()
        self.my_cards_deck.deal_one() # use the deal one on one of
                                      # the cards deck
        self.assertEqual(other_cards_deck, self.my_cards_deck.cards)
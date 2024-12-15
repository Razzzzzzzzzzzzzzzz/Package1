from unittest import TestCase
from Game_Cards.Card import Card
from Game_Cards.DeckOfCards import DeckOfCards

class TestDeckOfCards(TestCase):

    def setUp(self):
        self.my_cards_deck = DeckOfCards()

    def test_init_valid_deck_length(self):
        self.assertEqual(52, len(self.my_cards_deck.cards))

    def test_init_valid_no_duplicates(self):
        """Testing for identical cards in the cards deck"""
        no_duplicates = True
        for card1 in range(52):
            for card2 in range(card1 + 1,52):
                if card1 == card2:
                    no_duplicates = False # if a card is identical to another card in the cards deck
        self.assertTrue(no_duplicates)

    def test_init_valid_shuffle(self):
        """Testing if an un-shuffled deck of cards is equal to a shuffled deck of cards.
        If all cards are equal, then the test will fail"""
        shuffled_cards_deck = DeckOfCards()
        shuffled_cards_deck.cards_shuffle()
        shuffled = False
        for i in range(52):
            if shuffled_cards_deck.cards[i] != self.my_cards_deck.cards[i]:
                shuffled = True # If two cards on the same index is identical, it's shuffled.
                break
        self.assertTrue(shuffled)

    def test_init_invalid_shuffle_empty(self):
        """Testing if the method works when attempting to shuffle an empty list."""
        self.my_cards_deck.cards = []
        self.my_cards_deck.cards_shuffle()
        self.assertEqual(self.my_cards_deck.cards, [])

    def test_deal_one_valid_remove_one_card(self):
        """Testing for 1 card to be removed from the cards deck."""
        dealt_cards_deck = self.my_cards_deck.cards.copy()
        self.my_cards_deck.deal_one()
        self.assertEqual(len(dealt_cards_deck) - 1, len(self.my_cards_deck.cards))

    def test_deal_one_valid_return_card(self):
        """Testing if the returned object is a card."""
        returned_card = self.my_cards_deck.deal_one()
        self.assertEqual(type(returned_card), Card)


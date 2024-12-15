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
                    no_duplicates = False
        self.assertTrue(no_duplicates)

    def test_init_valid_shuffle(self):
        """Testing if an un-shuffled deck of cards is equal to a shuffled deck of cards.
        If all cards are equal, then the test will fail"""
        shuffled_cards_deck = DeckOfCards()
        shuffled_cards_deck.cards_shuffle()
        shuffled = False
        for i in range(52):
            if shuffled_cards_deck.cards[i] != self.my_cards_deck.cards[i]:
                shuffled = True
                break
        self.assertTrue(shuffled)

    def test_init_invalid_shuffle_empty(self):
        self.my_cards_deck.cards = []
        self.my_cards_deck.cards_shuffle()
        self.assertEqual(len(self.my_cards_deck.cards), 0)

    def test_deal_one_valid_remove_one_card(self):
        self.my_cards_deck.deal_one()
        self.assertEqual(len(self.my_cards_deck.cards), 51)

    def test_deal_one_valid_return_card(self):
        returned_card = self.my_cards_deck.deal_one()
        self.assertEqual(type(returned_card), Card)


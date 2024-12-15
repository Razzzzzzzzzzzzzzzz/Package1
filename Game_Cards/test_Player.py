from unittest import TestCase, mock
from Game_Cards.DeckOfCards import DeckOfCards
from Game_Cards.Player import Player
from Game_Cards.Card import Card

class TestPlayer(TestCase):

    def setUp(self):
        self.player1 = Player("Raz", 26)

    def test_init_valid_name(self):
        self.assertEqual(self.player1.name,"Raz")

    def test_init_valid_cards_number(self):
        self.assertEqual(self.player1.cards_number,26)

    def test_init_valid_cards_number_default_value(self):
        player2 = Player("Raz")
        self.assertEqual(player2.cards_number,26)

    def test_init_invalid_cards_value(self):
        player2 = Player("Raz", 50)
        self.assertEqual(player2.cards_number, 26)

    def test_init_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Player(5)

    def test_init_invalid_name_value(self):
        with self.assertRaises(ValueError):
            Player("")

    def test_set_hand_valid_length(self):
        cards_deck = DeckOfCards()
        self.player1.set_hand(cards_deck)
        self.assertEqual(len(self.player1.player_cards), 26)

    @mock.patch('Game_Cards.DeckOfCards.DeckOfCards.deal_one', return_value=Card(5,2))
    def test_set_hand_valid_type(self, mock_deal_one):
        """Tests if the player cards are of a card type"""
        cards_deck = DeckOfCards()
        self.player1.set_hand(cards_deck)
        self.assertEqual(type(self.player1.player_cards[0]), type(cards_deck.cards[0]))

    def test_set_hand_invalid_empty_deck(self):
        """To ensure the set hand method doesn't give an error when the cards deck is empty"""
        cards_deck = DeckOfCards()
        cards_deck.cards = []
        self.player1.set_hand(cards_deck)
        self.assertEqual(len(self.player1.player_cards), 0)

    def test_set_hand_invalid_type(self):
        """To raise an alert when the type is not a Card"""
        with self.assertRaises(TypeError):
            self.player1.set_hand(7)

    def test_get_hand_valid(self):
        """Ensures the get hand method returns a Card after being used"""
        self.player1.set_hand()
        self.assertEqual(type(self.player1.get_card()), type(self.player1.player_cards[0]))

    def test_get_hand_invalid_empty(self):
        self.assertEqual(self.player1.get_card(), None)

    def test_add_card_valid(self):
        cards_deck = DeckOfCards()
        self.player1.add_card(cards_deck.deal_one())
        self.assertEqual(len(self.player1.player_cards), 1)

    def test_add_card_invalid_type(self):
        self.player1.add_card(5)
        self.assertEqual(len(self.player1.player_cards), 0)
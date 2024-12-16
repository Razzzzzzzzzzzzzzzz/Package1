from unittest import TestCase, mock
from Game_Cards.DeckOfCards import DeckOfCards
from Game_Cards.Player import Player
from Game_Cards.Card import Card

class TestPlayer(TestCase):

    def setUp(self):
        self.player1 = Player("Raz", 26)

    def test_init_valid_name(self):
        """Testing for the name assignment to the player"""
        self.assertEqual(self.player1.name,"Raz")

    def test_init_valid_cards_number(self):
        """Testing the cards number assignment to the player"""
        self.assertEqual(self.player1.cards_number,26)

    def test_init_valid_cards_number_default_value(self):
        """checks if no card number was entered, will insert a default value of 26"""
        player2 = Player("Raz")
        self.assertEqual(player2.cards_number,26)

    def test_init_invalid_cards_value_high(self):
        """Tests for the return of a default value in case the cards number is too high"""
        player2 = Player("Raz", 50)
        self.assertEqual(player2.cards_number, 26)

    def test_init_invalid_cards_value_low(self):
        """Tests for the return of a default value in case the cards number is too low"""
        player2 = Player("Raz", 5)
        self.assertEqual(player2.cards_number, 26)

    def test_init_invalid_name_type(self):
        """Tests for an error to be given when giving an invalid type of name"""
        with self.assertRaises(TypeError):
            Player(5)

    def test_init_invalid_name_value_empty(self):
        """Tests for a value alert to be given when the player name is empty"""
        with self.assertRaises(ValueError):
            Player("")

    def test_set_hand_valid_length(self):
        """Tests for the set_hand card to give the player "player_cards" cards"""
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
        self.player1.set_hand() # For the player to have a cards deck to take a card from
        self.assertEqual(type(self.player1.get_card()), type(self.player1.player_cards[0]))

    def test_get_hand_invalid_empty(self):
        """Ensures the method does nothing if given an empty cards deck"""
        player_old_cards_deck = self.player1.player_cards.copy()
        self.player1.get_card()
        self.assertEqual(self.player1.player_cards, player_old_cards_deck)

    def test_add_card_valid(self):
        """Tests if a card was added after giving it one card"""
        cards_deck = DeckOfCards()
        player1_old_cards_deck = self.player1.player_cards.copy()
        self.player1.add_card(cards_deck.deal_one())
        self.assertEqual(len(self.player1.player_cards), len(player1_old_cards_deck) + 1)

    def test_add_card_invalid_type(self):
        """Tests for the method to not run if given a different type than a card"""
        player1_old_cards_deck = self.player1.player_cards.copy()
        self.player1.add_card(5)
        self.assertEqual(self.player1.player_cards, player1_old_cards_deck)
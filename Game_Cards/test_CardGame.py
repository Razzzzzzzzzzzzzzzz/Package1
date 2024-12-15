from unittest import TestCase
from Game_Cards.CardGame import CardGame
from Game_Cards.DeckOfCards import DeckOfCards
from unittest.mock import patch
from Game_Cards.Player import Player

class TestCardGame(TestCase):

    def setUp(self):
        self.game1 = CardGame("Raz", "Player", 10)

    def test_init_valid_name_one(self):
        self.assertEqual(self.game1.player_one.name, "Raz")

    def test_init_valid_name_two(self):
        self.assertEqual(self.game1.player_two.name, "Player")

    def test_init_valid_cards_number(self):
        self.assertEqual(self.game1.player_one.cards_number, 10)

    def test_init_invalid_name_one_value(self):
        with self.assertRaises(ValueError):
            CardGame("Raz", "")

    def test_init_invalid_name_two_value(self):
        with self.assertRaises(ValueError):
            CardGame("", "Player")

    def test_init_invalid_name_one_type(self):
        with self.assertRaises(TypeError):
            CardGame("Raz", 8)

    def test_init_invalid_name_two_type(self):
        with self.assertRaises(TypeError):
            CardGame(8, "Player")

    def test_init_invalid_cards_number_empty(self):
        self.game1 = CardGame("Raz", "Player")
        self.assertEqual(self.game1.player_one.cards_number, 26)

    def test_init_invalid_cards_number_high(self):
        self.game1 = CardGame("Raz", "Player", 200)
        self.assertEqual(self.game1.player_one.cards_number, 26)

    def test_init_invalid_cards_number_type(self):
        with self.assertRaises(TypeError):
            CardGame("Raz", "Player", "string")

    def test_new_game_valid_called_from_init(self):
        """Testing if 20 cards has been distributed from the cards deck by new_game method after only calling init method."""
        self.assertEqual(32, len(self.game1.game_cards_deck.cards))

    def test_new_game_invalid_called_from_outside_init(self):
        """Testing if the new_game method can be called from out of the init method."""
        player1_cards = self.game1.player_one.player_cards.copy()
        player2_cards = self.game1.player_two.player_cards.copy()
        deck_cards = self.game1.game_cards_deck.cards.copy()
        self.game1.new_game()
        self.assertTrue(deck_cards == self.game1.game_cards_deck.cards and player1_cards == self.game1.player_one.player_cards
                        and player2_cards == self.game1.player_two.player_cards)

    def test_new_game_valid_player_1_cards_amount(self):
        self.assertEqual(len(self.game1.player_one.player_cards), self.game1.player_one.cards_number)

    def test_new_game_valid_player_2_cards_amount(self):
        self.assertEqual(len(self.game1.player_two.player_cards), self.game1.player_two.cards_number)

    def test_get_winner_valid_player1_wins(self):
        self.player1_cards = self.game1.player_one
        self.player2_cards = self.game1.player_two
        self.player2_cards.get_card()
        self.assertEqual(self.game1.player_one, self.game1.get_winner())

    def test_get_winner_valid_player1_loses(self):
        self.player1_cards = self.game1.player_one
        self.player2_cards = self.game1.player_two
        self.player1_cards.get_card()
        self.assertEqual(self.game1.player_two, self.game1.get_winner())

    def test_get_winner_valid_draw(self):
        self.assertEqual(None, self.game1.get_winner())
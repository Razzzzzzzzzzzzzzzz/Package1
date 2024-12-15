from unittest import TestCase
from Game_Cards.Card import Card

class TestCard(TestCase):

    def setUp(self):
        self.my_card = Card(2,1)

    def test_init_valid_value(self):
        self.assertEqual(self.my_card.value, 2)

    def test_init_valid_symbol(self):
        self.assertEqual(self.my_card.symbol, 1)

    def test_init_invalid_value_type(self):
        with self.assertRaises(TypeError):
            Card("Hello", 2)

    def test_init_invalid_value_range_below(self):
        """If the card value is above the allowed value range, it will give a default value."""
        invalid_value_card = Card(20,1)
        self.assertEqual(invalid_value_card.value, 14)

    def test_init_invalid_value_range_above(self):
        """If the card value is under the allowed value range, it will give a default value."""
        invalid_value_card = Card(0,1)
        self.assertEqual(invalid_value_card.value, 14)

    def test_init_invalid_value_negative(self):
        invalid_value_card = Card(-1,1)
        self.assertEqual(invalid_value_card.value, 14)

    def test_init_invalid_symbol_value(self):
        with self.assertRaises(TypeError):
            Card(5, "Hello")

    def test_init_invalid_symbol_range_below(self):
        """If the card symbol is under the symbol allowed range, it will give a default value."""
        invalid_value_card = Card(1, 0)
        self.assertEqual(invalid_value_card.symbol, 1)

    def test_init_invalid_symbol_range_above(self):
        """If the card symbol is above the symbol allowed range, it will give a default value."""
        invalid_value_card = Card(1, 10)
        self.assertEqual(invalid_value_card.symbol, 1)

    def test_init_invalid_symbol_negative(self):
        invalid_value_card = Card(1, -1)
        self.assertEqual(invalid_value_card.symbol, 1)

    def test_gt_valid_higher_value(self):
        higher_card = Card(10,1)
        self.assertGreater(higher_card, self.my_card)

    def test_gt_valid_higher_symbol(self):
        higher_card = Card(2,4)
        self.assertGreater(higher_card, self.my_card)

    def test_gt_valid_ace_highest(self):
        """Ensures that Ace is the highest card"""
        king_card = Card(13,1)
        ace_card = Card(1,1)
        self.assertGreater(ace_card, king_card)

    def test_gt_invalid_value(self):
        other_card = Card(5, 1)
        self.assertFalse(self.my_card > other_card)

    def test_gt_invalid_symbol(self):
        other_card = Card(2, 4)
        self.assertFalse(self.my_card > other_card)

    def test_eq_valid_value(self):
        other_card = Card(2,1)
        self.assertEqual(self.my_card,other_card)

    def test_eq_invalid_value(self):
        other_card = Card(3,1)
        self.assertFalse(self.my_card == other_card)

    def test_eq_invalid_symbol(self):
        other_card = Card(2,2)
        self.assertFalse(self.my_card == other_card)
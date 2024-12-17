from unittest import TestCase
from Game_Cards.Card import Card

class TestCard(TestCase):

    def setUp(self):
        """Creates a card before every method runs"""
        self.my_card = Card(2,1)

    # -----[Init Testing]-----
    def test_init_valid_value(self):
        """checks if the value the user gives enters as the
         card value"""
        self.assertEqual(2, self.my_card.value)

    def test_init_valid_symbol(self):
        """checks if the symbol the user gives enters as the
         card symbol"""
        self.assertEqual(1, self.my_card.symbol)

    def test_init_invalid_value_type(self):
        """tests for an error to be given when giving a non-int type
         of value"""
        with self.assertRaises(TypeError):
            Card("Hello", 2)

    def test_init_invalid_value_range_below(self):
        """If the card value is under the allowed value range,
         it will give a default value."""
        invalid_value_card = Card(0,1)
        self.assertEqual(invalid_value_card.value, 14)

    def test_init_invalid_value_range_above(self):
        """If the card value is above the allowed value range, it will
         give a default value."""
        invalid_value_card = Card(15,1)
        self.assertEqual(14, invalid_value_card.value)

    def test_init_invalid_value_negative(self):
        """tests for a default value to be given when entering a
         negative value as the user."""
        invalid_value_card = Card(-1,1)
        self.assertEqual(14, invalid_value_card.value)

    def test_init_invalid_symbol_value(self):
        """tests for an error when giving a non-int type of symbol."""
        with self.assertRaises(TypeError):
            Card(5, "Hello")

    def test_init_invalid_symbol_range_below(self):
        """If the card symbol is under the symbol allowed range,
         it will give a default value."""
        invalid_value_card = Card(1, 0)
        self.assertEqual(1, invalid_value_card.symbol)

    def test_init_invalid_symbol_range_above(self):
        """If the card symbol is above the symbol allowed range,
         it will give a default value."""
        invalid_value_card = Card(1, 10)
        self.assertEqual(1, invalid_value_card.symbol)

    def test_init_invalid_symbol_negative(self):
        """tests for a default value when giving a negative value
         in the symbol"""
        invalid_value_card = Card(1, -1)
        self.assertEqual(1, invalid_value_card.symbol)

    #-----[gt testing]-----
    def test_gt_valid_higher_value(self):
        """ensures the greater method returns true when the value
         is higher"""
        higher_card = Card(10,1)
        self.assertGreater(higher_card, self.my_card)

    def test_gt_valid_higher_symbol(self):
        """tests if the greater method returns true when the values
         are equal but the symbol is higher."""
        higher_card = Card(2,4)
        self.assertGreater(higher_card, self.my_card)

    def test_gt_valid_ace_highest(self):
        """Testing if Ace is the highest card by comparing it to
        the king card."""
        king_card = Card(13,1)
        ace_card = Card(1,1)
        self.assertGreater(ace_card, king_card)

    def test_gt_valid_false_value(self):
        """Testing if the greater method returns false when the
        card is not higher."""
        other_card = Card(5, 1)
        self.assertFalse(self.my_card > other_card)

    def test_gt_valid_false_symbol(self):
        """Testing if the greater method returns false when the
        value is identical and the symbol is lower"""
        other_card = Card(2, 4)
        self.assertFalse(self.my_card > other_card)

    def test_gt_valid_false_equal(self):
        """Testing if the greater method returns false when
        the cards are equal"""
        other_card = self.my_card
        self.assertFalse(self.my_card > other_card)

    def test_gt_invalid_type(self):
        """Testing for an error when giving an invalid
        type instead of a card"""
        with self.assertRaises(TypeError):
            self.my_card > 5

    #-----[eq testing]-----
    def test_eq_valid(self):
        """Testing the equal method with two cards with the
        same info."""
        other_card = Card(2,1)
        self.assertEqual(other_card, self.my_card)

    def test_eq_valid_false_value(self):
        """Testing if the equal method will return false when
        both values are different"""
        other_card = Card(3,1)
        self.assertFalse(self.my_card == other_card)

    def test_eq_valid_false_symbol(self):
        """Testing if the equal method will return false when
        both values are different"""
        other_card = Card(2,2)
        self.assertFalse(self.my_card == other_card)

    def test_eq_invalid_type(self):
        """Testing for an error when giving an invalid
        type instead of a card"""
        with self.assertRaises(TypeError):
            self.my_card == 5
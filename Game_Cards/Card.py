class Card:
    def __init__(self, value, symbol):
        MIN_CARD = 2
        MAX_CARD = 13
        ACE_VALUE = 14
        if type(value) != int:
            raise TypeError("Value must be an int!")
        if  MIN_CARD <= value <= MAX_CARD:
            self.value = value
        else:
            self.value = ACE_VALUE # Default Value and assign Ace with
                            # the highest value
        MIN_SYMBOL = 1
        MAX_SYMBOL = 4
        if type(symbol) != int:
            raise TypeError("Symbol must be an int!")
        if MIN_SYMBOL <= symbol <= MAX_SYMBOL:
            self.symbol = symbol
        else:
            self.symbol = MIN_SYMBOL

    def __gt__(self, other):
        """To determine if this card is bigger in value than the other
         card, or in symbol if their value is equal."""
        if self.value > other.value:
            return True
        elif self.value < other.value:
            return False
        else:
            return self.symbol > other.symbol # Since two cards that are
                                              # alike do not exist.

    def __eq__(self, other):
        """To determine if both cards are equal in value and are with
         an identical symbol."""
        return self.value == other.value and self.symbol == other.symbol

    def __str__(self):
        """To return special cards with their name instead of
         a number."""
        if self.value == 14:
            card_value = "Ace"
        elif self.value == 11:
            card_value = "Jack"
        elif self.value == 12:
            card_value = "Queen"
        elif self.value == 13:
            card_value = "King"
        else:
            card_value = self.value
        if self.symbol == 1:
            card_symbol = "Diamonds ♦"
        elif self.symbol == 2:
            card_symbol = "Spades ♠"
        elif self.symbol == 3:
            card_symbol = "Hearts ♥"
        else:
            card_symbol = "Clubs ♣"
        return f"|{card_value} of {card_symbol}|"

    def __repr__(self):
        """for special card names when running through an entire
         cards deck"""
        if self.value == 14:
            card_value = "Ace"
        elif self.value == 11:
            card_value = "Jack"
        elif self.value == 12:
            card_value = "Queen"
        elif self.value == 13:
            card_value = "King"
        else:
            card_value = self.value
        if self.symbol == 1:
            card_symbol = "Diamonds ♦"
        elif self.symbol == 2:
            card_symbol = "Spades ♠"
        elif self.symbol == 3:
            card_symbol = "Hearts ♥"
        else:
            card_symbol = "Clubs ♣"
        return f"|{card_value} of {card_symbol}|"
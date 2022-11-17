from suit import Suit


class Card:
    SPECIAL_CARDS = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def is_special(self):
        if self._value >= 11:
            return True
        return False

    def show(self):
        if self.is_special():
            desc = Card.SPECIAL_CARDS[self._value]
            print(f"{desc} of {self._suit.suit_name}")
        else:
            print(f"{self._value} of {self._suit.suit_name}")


one = Card(Suit("hearts"), 1)
print(one.is_special())
print(one.show())
eleven = Card(Suit("hearts"), 11)
print(eleven.is_special())
print(eleven.show())

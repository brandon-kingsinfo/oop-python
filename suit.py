class Suit:
    SYMBOLS = {"clubs": "♣", "diamaonds": "♦", "hearts": "♥", "spades": "♠"}

    def __init__(self, suit_name):
        self._suit_name = suit_name
        self._symbol = Suit.SYMBOLS.get(suit_name.lower(), None)

    @property
    def suit_name(self):
        return self._suit_name

    @property
    def symbol(self):
        return self._symbol


clubs = Suit("clubs")

print(clubs.symbol)

class CardGame:
    def __init__(self, player, computer, deck) -> None:
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, player):
        for i in range(26):
            player.deck.add(self._deck.draw())

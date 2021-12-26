    """Käynnistetään peli ja määritetään pelialueen koko.
    """
from game import Game
SIZE = 20  # pelialueen koko
new_game = Game(SIZE)
new_game.loop()

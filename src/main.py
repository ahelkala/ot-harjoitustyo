# Täältä käynnistetään peli ja määritetään pelialueen koko
# Tulevaisuudessa täällä hoidetaan tietokantaan liittyvät tehtävät
# sekä muiden peliparametrien välitys pelille???
#

from game import Game
SIZE = 9        #pelialueen koko
new_game = Game(SIZE)
new_game.loop()

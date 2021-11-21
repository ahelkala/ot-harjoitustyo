# Täältä käynnistetään peli ja määritetään pelialueen koko
# Tulevaisuudessa täällä hoidetaan tietokantaan liittyvät tehtävät sekä muiden peliparametrien välitys pelille???
#

from game import Game
size = 9        #pelialueen koko
new_game = Game(size)
new_game.loop()
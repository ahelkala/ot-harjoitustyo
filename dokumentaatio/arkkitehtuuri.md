# Arkkitehtuurikuvaus

## Rakenne
Luokka *Draw* sisältää käyttöliittymän koodin. Luokka *Game* sisältää hoitaa pelin logiikan, lukuun ottamatta miinakentän ylläpitoa, jonka hoitaa luokka *GameGrid*. Läpäistyjen pelien tulokset tallennetaan ja luetaan luokasta *DataBaseConnection*

<img src="https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luokkakaavio3.png" width="750">

## Tietojen tallennus
Pelitulokset tallennetaan SQLite-tietokantaan. Tietokantaan luodaan myös sen luonnin yhteydessä valmiita tuloksia, jotta tuloslistalla olisi heti näytettävää. 

## Käyttöliittymä
Käyttöliittymä sisältää pelialueen, yläreunan infolaatikon sekä pelin lopuksi pelialueen päälle piirrettävän tuloslistan.

## Pelin käynnistyminen luokkakaaviona
<img src="https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/gamestart.png" width="750">
Ohjelma käynnistyy luomalla Game-olion, joka alustaa Pygame-moduulin, peliruudukon ja piirtää sen jälkeen piirtää peliruudukon numeerisia arvoja vastaavan pelialueen sekä käyttöliittymän yläreunassa sijaitsevan info-alueen.

## Ohjelman heikkoudet
Ohjelman luokkien toiminnallisuuksiin jäi päällekkäisyyksiä. Esimerkiksi luokassa Game ja Draw käsitellään samaa dataa osittain päällekkäin. Ohjelman luokat tulisi suunnitella tarkemmin. Luokkien toteutuksen haasteet myös hankaloittivat testien kirjoittamista eri toiminnallisuuksille, joista osa jäi täysin testien ulkopuolelle. 

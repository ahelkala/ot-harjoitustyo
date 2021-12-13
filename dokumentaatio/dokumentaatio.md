# Käyttöohje

## Asentaminen sekä käynnistäminen
Lataa ohjelmiston uusin versio [täältä](https://github.com/ahelkala/ot-harjoitustyo/releases). Jos koneellesi ei ole jo asennettu vähintään Pythonin versiota 3.8, voit hakea sen asennuspaketin [täältä](https://www.python.org/downloads/).
Ohjelmiston riippuvuuksien hallinnassa käytetyn Poetryn voi tarvittaessa asentaa komennolla:

```bash
pip3 install poetry
```

Ohjelman vaatimat riippuvuudet asentuvat komennolla:
```bash
poetry install
```
Tämän jälkeen alusta ympäristö komennolla:
```bash
poetry run invoke build
```
Ohjelman voi nyt käynnistää komennolla:
```bash
poetry run invoke start
```
## Käyttöliittymä
Esimerkki käynnissä olevasta pelistä

<img src="https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/minesweeper.png" width="400">

### Toiminnot
- Hiiren vasen painike avaa ruudun
- Hiiren oikea painike lisää tai poistaa lipun, jolla voi merkitä miinaksi epäillyn ruudun
- Välilyönti käynnistää pelin uudelleen
- Oikean yläkulman ruksilla suljetaan ohjelma

## Pelin kulku
Käyttäjä avaa ruutuja ja yrittää välttää osumasta pelialueelle sattumanvaraisiin ruutuihin asetettuja miinoja. Miinojen paikkoja voi päätellä pelialueella olevien numeeristen vihjeiden avulla. Numeron ollessa yksi, ruudun ympärillä sijaitsee yksi miina. Numeron ollessa kaksi, ruudun ympärillä on kaksi miinaa jne. Päättelyä voi helpottaa merkitsemällä miinoiksi epäilemänsä ruudut lipuilla.

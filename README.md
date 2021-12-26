# Miinaharava

Sovellus on mukaelma perinteisestä Miinaharava-pelistä. Peli on yksinpeli, jonka tarkoituksena on löytää miinakentälle kätketyt miinat mahdollisimman nopeasti. Peli päättyy tappioon, jos pelaaja osuu miinaan.

## Dokumentaatio

[Käyttöohje](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

[Vaatimusmäärittely](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)

[Työaikakirjanpito](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Riippuvuuksien asentaminen:
```bash
poetry install
```

2. Sovelluksen käynnistäminen:
```bash
poetry run invoke start
```
## Komentorivitoiminnot

### Ohjelman suorittaminen:

Sovelluksen käynnistäminen:
```bash
poetry run invoke start
```
### Testaus

Aja testit komennolla:
```bash
poetry run invoke test
```
### Testikattavuus

Testikattavuuden raportti:
```bash
poetry run invoke coverage-report
```
Html-version raportista saa avaamalla tiedoston htmlcov/index.html

### Pylint

Pylintin tarkistukset voi ajaa komennolla:
```bash
poetry run invoke lint
```
### Lähteet
Pelissä käytetyt kuvat tehnyt OpenGameArt.Org -sivustolla nimimerkki Eugeneloza (https://opengameart.org/content/minesweeper-tile-set-lazarus). Lisenssi "Feel free to use :)".

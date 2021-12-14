# Miinaharava

Tänne rakentuu pikkuhiljaa Miinaharavan kaltainen peli. 

[Release viikko 6](https://github.com/ahelkala/ot-harjoitustyo/releases/tag/viikko6)

[Release viikko 5](https://github.com/ahelkala/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

[Käyttöohje](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)

[Työaikakirjanpito](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus
1. Riippuvuuksien asentaminen:
```bash
poetry install
```
2. Suorita alustustoimenpiteet:
```bash
poetry run invoke build
```

3. Sovelluksen käynnistäminen:
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

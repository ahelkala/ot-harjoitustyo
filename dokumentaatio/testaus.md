# Testausdokumentti

## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka
Sovelluslogiikkaa testataan TestGame- sekä TestGameGrid-testiluokilla. 

### Tietokanta
Tietokannan toimintaa testataan TestDataBaseConnection-luokalla. Tietokannan testaamisessa on huomioitu Game-luokan testien tietokantaan luomat tietueet.


### Testauskattavuus
Pelin testauksen haaraumakattavuus on 74%.
![](./kuvat/testikattavuus.png)
Testaus jäi varsinkin Game-luokan osalta vajaaksi. Testien kirjoittaminen oli ohjelman rakenteen vuoksi hankalaa ja rakennetta tulisikin hieman korjata mm. tämän syyn takia.

## Järjestelmätestaus
Sovelluksen asentaminen on testattu macOS- sekä Linux-ympäristöissä [käyttöohjetta](https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) noudattaen. 

Tietokannan toimintaa on testattu valmiilla tietokannalla sekä annettu sovelluksen luoda se itse. 

Pelin erilaisia skenaarioita on testattu manuaalisesti. Sovelluksesta ei ole löytynyt sen kaatavia bugeja tai virheellisesti toimivia toiminnalisuuksia.

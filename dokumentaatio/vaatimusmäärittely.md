# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on miinaharava-tyyppinen peli, jossa yritetään löytää piilotetut miinat pelikentältä löytyvien numeeristen vihjeiden avulla. Tulokset tallennetaan tietokantaan.

## Käyttäjät

Voittaessaan pelin käyttäjä saa nimensä kunniataulukkoon. Itse pelaaminen ei vaadi käyttäjältä nimen antamista tai kirjautumista.

## Käyttöliittymäluonnos

<img src="https://github.com/ahelkala/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoliittyma.png" width="750">

Sovelluksessa on kaksi näkymää. Itse pelinäkymä ja sen päällä pelin päätteeksi näkyvä kunniataulukko parhaille tuloksille. 

## Perusversion tarjoama toiminnallisuus
### Pelissä

- käyttäjä voi merkata miinoiksi epäilemänsä ruudut 
- käyttäjälle näytetään miinojen viereisissä ruuduissa numeerinen vihje montako miinaa kyseisen ruudun ympärillä on 
- käyttäjä näkee jäljellä olevien miinojen määrän laskurista 
- käyttäjälle näytetään peliin käytetty aika
- kun kaikki muut ruudut on miinoja lukuunottamatta on avattu, käyttäjä voittaa pelin 
- jos käyttäjä osuu miinaan, peli päättyy 

### Voiton tai tappion jälkeen

- käyttäjälle näytetään tietokannasta viiden parhaimman tuloksen kunniataulukko

## Jatkokehitysideoita

- käyttäjä voi määritellä miinojen määrän sekä peliruudukon koon
- parhaimpien tulosten muistaminen eri peliruudukon kokojen sekä miinojen määrän perusteella tai vaihtoehtoisesti useampi vakioitu peliruudukko miinoineen
- "ehkä miina"-merkinnän lisääminen

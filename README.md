# Tyotehtavien-Automatisointi-Komentokielella

# Säähakuskripti

## 1. Skriptin tarkoitus
Tämä ohjelma hakee säätiedot halutuista kaupungeista Open-Meteo API:n avulla ja näyttää ne käyttäjälle tai tallentaa ne lokitiedostoon.

- **Interaktiivinen versio (`ui.py`)**  
  Kysyy käyttäjältä kaupungin nimen, näyttää nykyisen lämpötilan, tuulen nopeuden ja suunnan sekä havainnoinnin ajan paikallisessa ajassa.  

- **Automaattinen versio (`automaatti.py`)**  
  Käy listan kaupungeista läpi, hakee säätiedot, tallentaa ne lokiin ja vertaa uutta lämpötilaa edelliseen mittaukseen.

---

2. Järjestelmävaatimukset
- **Python 3.9+**  
- Internet-yhteys API-kutsuja varten  
- Tarvittavat Python-kirjastot:
  pip install requests

Siirrettävyys
- Skripti toimii kaikilla koneilla, joilla on Python 3.9+ ja internet-yhteys.

Mahdolliset rajoitteet
- Ohjelma näyttää vain nykyisen sään (current_weather) eikä ennusteita.
- Jos kaupunkia ei löydy API:sta, ohjelma ilmoittaa, ettei säätietoja saatu.
- Ohjelma ei käsittele virheellisiä syötteitä kovin monipuolisesti; käyttäjän pitää syöttää oikea kaupungin nimi.

Kehitys
- Lisää mahdollisuus hakea säätiedot useamman päivän ennusteena.

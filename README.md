# Tyotehtavien-Automatisointi-Komentokielella

# Säähakuskripti

## 1. Skriptin tarkoitus
Tämä ohjelma hakee säätiedot halutuista kaupungeista Open-Meteo API:n avulla ja näyttää ne käyttäjälle tai tallentaa ne lokitiedostoon.

- **Interaktiivinen versio (`ui.py`)**  
  Kysyy käyttäjältä kaupungin nimen, näyttää nykyisen lämpötilan, tuulen nopeuden ja suunnan sekä havainnoinnin ajan paikallisessa ajassa.  

- **Automaattinen versio (`automaatti.py`)**  
  Käy listan kaupungeista läpi, hakee säätiedot, tallentaa ne lokiin ja vertaa uutta lämpötilaa edelliseen mittaukseen.

---

## 2. Järjestelmävaatimukset
- **Python 3.9+**  
- Internet-yhteys API-kutsuja varten  
- Tarvittavat Python-kirjastot:
  pip install requests

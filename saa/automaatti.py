from core import hae_saa   # Tuodaan toisesta tiedostosta funktio,
                          # joka hakee säätiedot kaupungille.
import datetime            # Tarvitaan nykyisen ajan hakemiseen lokiin.
import os                  # Käytetään tarkistamaan onko lokitiedosto olemassa.


# Lista kaupungeista joista säätiedot haetaan.
# Voit muuttaa tätä listaa vapaasti.
kaupungit = ["Helsinki", "Tampere", "Turku"]

# Lokitiedoston nimi.
# Sama tiedosto säilyttää kaikki mittaukset.
LOKI = "saa_loki.txt"

# Tämä funktio etsii lokitiedostosta viimeisimmän
# lämpötilan tietylle kaupungille.
#
# Tätä käytetään vertailuun:
# → onko nyt lämpimämpää vai kylmempää kuin viimeksi.
# -----------------------------------------
def hae_vanha_lampotila(city):

    # Jos lokitiedostoa ei ole vielä olemassa,
    # ei ole myöskään vanhaa dataa.
    if not os.path.exists(LOKI):
        return None

    # Avataan tiedosto lukutilassa ("r")
    # encoding="utf-8" varmistaa että ääkköset toimii.
    with open(LOKI, "r", encoding="utf-8") as f:
        rivit = f.readlines()

    # Käydään rivit LOPUSTA alkuun,
    # koska viimeinen rivi on uusin mittaus.
    for rivi in reversed(rivit):

        # Tarkistetaan että rivi kuuluu oikealle kaupungille
        # ja että siinä on lämpötila.
        if city in rivi and "°C" in rivi:
            try:
                # Rivi on muotoa:
                # [aika] Kaupunki | 10 °C | Tuuli ...
                #
                # split("|") jakaa tekstin pystypalkin kohdalta.
                osa = rivi.split("|")[1]

                # Poistetaan turhat välilyönnit ja °C-merkintä.
                lampo = osa.strip().replace("°C", "")

                # Muutetaan merkkijono numeroksi.
                #Eli rivi ottaa lämpöarvon ja palauttaa sen numerona, jotta sillä voi tehdä laskuja.
                return float(lampo)

            except:
                # Jos rivin käsittely epäonnistuu,
                # palautetaan None turvallisesti.
                return None

    # Jos sopivaa riviä ei löytynyt:
    return None

# Avataan lokitiedosto lisäystilassa ("a"):
# → vanhat tiedot säilyvät
# → uusi data lisätään loppuun.
with open(LOKI, "a", encoding="utf-8") as f:

    for city in kaupungit:

        # Haetaan säätiedot core.py -tiedoston funktiolla.
        data = hae_saa(city)

        # Nykyinen päivämäärä ja kellonaika.
        aika = datetime.datetime.now()

        if data:
            # Uusi lämpötila API:sta
            uusi_lampo = data["temperature"]

            # Haetaan vanha lämpötila lokista
            vanha_lampo = hae_vanha_lampotila(city)

            if vanha_lampo is None:
                muutos = "(ei vertailutietoa)"
            elif uusi_lampo > vanha_lampo:
                muutos = "lämpimämpää kuin viimeksi"
            elif uusi_lampo < vanha_lampo:
                muutos = "kylmempää kuin viimeksi"
            else:
                muutos = "sama lämpötila"

            # Rakennetaan lokirivi.
            # f-string mahdollistaa muuttujien
            # lisäämisen suoraan tekstin sekaan.
            rivi = (
                f"[{aika}] {data['city']}, {data['country']} | "
                f"{uusi_lampo} °C | "
                f"Tuuli {data['windspeed']} km/h | "
                f"{muutos}\n"
            )

        else:
            # Jos säätietoa ei saatu:
            rivi = f"[{aika}] {city} | Ei säätietoja\n"

        # Kirjoitetaan rivi lokitiedostoon.
        f.write(rivi)







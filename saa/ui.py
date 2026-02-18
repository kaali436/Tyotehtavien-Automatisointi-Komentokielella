# Tuodaan säähakufunktio toisesta tiedostosta.
from core import hae_saa
from datetime import datetime, timezone  # Tarvitaan nykyisen ajan hakemiseen lokiin.



# while True = jatkuva silmukka.
# Ohjelma kysyy kaupungin nimeä niin kauan,
# kunnes käyttäjä itse lopettaa.
while True:

    # input() odottaa käyttäjän syötettä.
    # strip() poistaa turhat välilyönnit.
    city = input("\nAnna kaupungin nimi (ENTER lopettaa): ").strip()

    # Jos käyttäjä painaa pelkkää Enteriä:
    if not city:
        print("Ohjelma lopetettu.")
        break  # poistutaan silmukasta

    # Kutsutaan ydinfunktion säähakua.
    data = hae_saa(city)

    # Jos data löytyi:

    if data:
        try:
            # Luetaan API:sta saatu aika merkkijonona ja muunnetaan datetime-objektiksi
            utc_time = datetime.fromisoformat(data['time'])
            # Merkitään tämä datetime-objekti selvästi UTC-ajaksi
            # Tämä kertoo Pythonille, että aika on UTC-aikaa
            utc_time = utc_time.replace(tzinfo=timezone.utc)
            local_time = utc_time.astimezone()  # Muutetaan paikalliseksi ajaksi
            aika_str = local_time.strftime("%d.%m.%Y %H:%M")     # Muodostetaan luettava merkkijono paikallisesta ajasta
        except ValueError:
            aika_str = data['time']

        
        print("\nSäätiedot:")

        # f-string helpottaa muuttujien tulostamista:
        # f"... {muuttuja} ..."
        
        print(f"Kaupunki: {data['city']}, {data['country']}")
        print(f"Lämpötila: {data['temperature']} °C")
        print(f"Tuulen nopeus: {data['windspeed']} km/h")
        print(f"Tuulen suunta: {data['winddirection']}°")
        print(f"Havaintoaika: {aika_str}")

        #kysytään käyttäjältä, haluaako hän tallentaa tiedot lokiin.
        tallenna = input("Haluatko tallentaa tiedot lokiin? (k/e): ").strip().lower()
        if tallenna == 'k':
            with open("saa_loki.txt", "a", encoding="utf-8") as loki:
                loki.write(
                    f"{aika_str} - {data['city']}, {data['country']} - "
                    f"Lämpö: {data['temperature']} °C, "
                    f"Tuuli: {data['windspeed']} km/h, {data['winddirection']}°\n"
                )
            print("Tiedot tallennettu lokiin.")

    else:
        # Jos API ei vastannut tai kaupunkia ei löytynyt.
        print("Säätietoja ei saatu.")

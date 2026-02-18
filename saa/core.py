import requests  # requests-kirjasto mahdollistaa HTTP-pyynnöt internetiin.
# Tämän avulla voidaan hakea tietoa API-palvelimilta.


def hae_saa(city):
    """
    Funktio hakee säätiedot annetulle kaupungille.

    Parametri:
        city (str) = kaupungin nimi tekstinä.

    Palauttaa:
        dict = säätiedot sanakirjana jos onnistuu
        None = jos jotain menee pieleen (esim. kaupunkia ei löydy).
    """
    # Sääpalvelu ei käytä kaupungin nimeä suoraan,
    # vaan tarvitsee leveys- ja pituusasteet (latitude, longitude).

    geo_base = "https://geocoding-api.open-meteo.com/v1/search"

    # API-parametrit lähetetään sanakirjana.
    # requests lisää nämä automaattisesti URLiin.
    geo_params = {
        "name": city,      # käyttäjän antama kaupungin nimi
        "count": 1,        # otetaan vain paras hakutulos
        "language": "fi",  # yritetään saada tiedot suomeksi
        "format": "json"   # vastaus JSON-muodossa
    }

    try:
        # GET-pyyntö palvelimelle:
        geo_response = requests.get(
            geo_base,
            params=geo_params,
            timeout=10  # maksimi odotusaika sekunneissa
        )

        # HTTP-statuskoodi kertoo onnistuiko pyyntö:
        # 200 = OK
        # 404 = ei löytynyt
        # 500 = palvelinvirhe jne.
        if geo_response.status_code != 200:
            return None

        # JSON-vastaus muutetaan Python-sanakirjaksi.
        geo_data = geo_response.json()

    except:
        # Jos netti ei toimi, DNS ei löydy tms.
        # ohjelma ei kaadu vaan palauttaa None.
        return None

    # Haetaan hakutulokset:
    # .get() ei aiheuta virhettä vaikka avain puuttuisi.
    results = geo_data.get("results")

    # Jos kaupunkia ei löytynyt:
    if not results:
        return None

    # Otetaan ensimmäinen tulos listasta.
    first = results[0]

    # Leveysaste ja pituusaste kartalla:
    latitude = first.get("latitude")
    longitude = first.get("longitude")

    # API:n virallinen nimi kaupungille.
    name = first.get("name", city)

    # Maa jossa kaupunki sijaitsee.
    country = first.get("country", "")

    # Nyt kun tiedetään sijainti kartalla,
    # voidaan hakea säätiedot.

    weather_base = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",  # pyydetään nykyinen sää
        "windspeed_unit": "kmh",    # tuulen nopeus km/h
    }

    try:
        weather_response = requests.get(
            weather_base,
            params=weather_params,
            timeout=10
        )

        if weather_response.status_code != 200:
            return None

        weather_data = weather_response.json()

    except:
        return None

    # Varsinainen säädata löytyy avaimen "current_weather" alta.
    weather = weather_data.get("current_weather")

    if not weather:
        return None

    # Rakennetaan selkeä sanakirja tiedoista,
    # jotta käyttöliittymä tai lokiohjelma voi käyttää sitä.

    return {
        "city": name,
        "country": country,
        "temperature": weather.get("temperature"),
        "windspeed": weather.get("windspeed"),
        "winddirection": weather.get("winddirection"),
        "time": weather.get("time"),
    }
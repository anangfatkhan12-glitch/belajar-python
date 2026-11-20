import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=-6.2&longitude=106.8&current=temperature_2m,weather_code,wind_speed_10m&timezone=Asia%2FJakarta"

arti_kode = {0: "Cerah", 1: "Sebagian besar cerah", 2: "Berawan sebagian", 3: "Mendung", 45: "Berkabut", 48: "Berkabut", 51: "Gerimis ringan", 53: "Gerimis", 55: "Gerimis lebat", 61: "Hujan ringan", 63: "Hujan sedang", 65: "Hujan lebat", 80: "Hujan lokal ringan", 81: "Hujan lokal sedang", 82: "Hujan lokal lebat", 95: "Badai petir"}

try:
    data = requests.get(url, timeout=15).json()
    c = data["current"]
    kode = c["weather_code"]
    print("=== CUACA JAKARTA ===")
    print(f"Waktu   : {c['time']}")
    print(f"Suhu    : {c['temperature_2m']} derajat Celcius")
    print(f"Kondisi : {arti_kode.get(kode, 'Kode tidak dikenal')} (kode {kode})")
    print(f"Angin   : {c['wind_speed_10m']} km/jam")
except Exception as e:
    print("Gagal mengambil data:", e)

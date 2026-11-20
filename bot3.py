import requests
import time

token = open("token.txt").read().strip()
dasar = f"https://api.telegram.org/bot{token}"
offset = 0

arti_kode = {0: "Cerah", 1: "Sebagian besar cerah", 2: "Berawan sebagian", 3: "Mendung", 45: "Berkabut", 48: "Berkabut", 51: "Gerimis ringan", 53: "Gerimis", 55: "Gerimis lebat", 61: "Hujan ringan", 63: "Hujan sedang", 65: "Hujan lebat", 80: "Hujan lokal ringan", 81: "Hujan lokal sedang", 82: "Hujan lokal lebat", 95: "Badai petir"}

def ambil_cuaca():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=-6.2&longitude=106.8&current=temperature_2m,weather_code,wind_speed_10m&timezone=Asia%2FJakarta"
        data = requests.get(url, timeout=15).json()
        c = data["current"]
        kondisi = arti_kode.get(c["weather_code"], "Tidak dikenal")
        return f"Cuaca Jakarta sekarang:\nSuhu: {c['temperature_2m']} derajat Celcius\nKondisi: {kondisi}\nAngin: {c['wind_speed_10m']} km/jam"
    except Exception:
        return "Maaf, data cuaca sedang tidak bisa diambil. Coba lagi nanti."

print("Bot Kasir Damian v3 berjalan. CTRL+C untuk berhenti.")

while True:
    try:
        data = requests.get(dasar + "/getUpdates", params={"offset": offset}, timeout=15).json()
        for upd in data["result"]:
            offset = upd["update_id"] + 1
            pesan = upd.get("message")
            if pesan is None or "text" not in pesan:
                continue
            chat_id = pesan["chat"]["id"]
            teks = pesan["text"]
            if teks == "/start":
                balasan = "Halo! Saya bot Kasir Damian. Perintah: /kasir = catatan penjualan, /cuaca = cuaca Jakarta sekarang."
            elif teks == "/kasir":
                balasan = "Catatan penjualan:\n" + open("penjualan.txt").read()
            elif teks == "/cuaca":
                balasan = ambil_cuaca()
            else:
                balasan = "Anda menulis: " + teks
            requests.post(dasar + "/sendMessage", data={"chat_id": chat_id, "text": balasan}, timeout=15)
    except Exception as e:
        print("Koneksi bermasalah:", e)
        print("Mencoba lagi dalam 3 detik...")
        time.sleep(3)
    time.sleep(1)

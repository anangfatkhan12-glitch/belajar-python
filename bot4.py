import requests
import time
from urllib.parse import urlparse

token = open("token.txt").read().strip()
dasar = f"https://api.telegram.org/bot{token}"
offset = 0

arti_kode = {0: "Cerah", 1: "Sebagian besar cerah", 2: "Berawan sebagian", 3: "Mendung", 45: "Berkabut", 48: "Berkabut", 51: "Gerimis ringan", 53: "Gerimis", 55: "Gerimis lebat", 61: "Hujan ringan", 63: "Hujan sedang", 65: "Hujan lebat", 80: "Hujan lokal ringan", 81: "Hujan lokal sedang", 82: "Hujan lokal lebat", 95: "Badai petir"}

resmi = {"facebook": "facebook.com", "instagram": "instagram.com", "google": "google.com", "tokopedia": "tokopedia.com", "tiktok": "tiktok.com", "whatsapp": "whatsapp.com", "github": "github.com"}

def ambil_cuaca():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=-6.2&longitude=106.8&current=temperature_2m,weather_code,wind_speed_10m&timezone=Asia%2FJakarta"
        data = requests.get(url, timeout=15).json()
        c = data["current"]
        kondisi = arti_kode.get(c["weather_code"], "Tidak dikenal")
        return f"Cuaca Jakarta sekarang:\nSuhu: {c['temperature_2m']} derajat Celcius\nKondisi: {kondisi}\nAngin: {c['wind_speed_10m']} km/jam"
    except Exception:
        return "Maaf, data cuaca sedang tidak bisa diambil. Coba lagi nanti."

def periksa_link(link):
    if "://" not in link:
        link = "https://" + link
    bagian = urlparse(link)
    domain = bagian.hostname or ""
    peringatan = []
    if bagian.scheme != "https":
        peringatan.append("Tidak memakai https (koneksi tidak terenkripsi)")
    if domain.replace(".", "").isdigit():
        peringatan.append("Domain berupa angka IP - situs resmi tidak login lewat alamat angka")
    for merek, domain_resmi in resmi.items():
        if merek in domain and domain != domain_resmi and not domain.endswith("." + domain_resmi):
            peringatan.append(f"Menyebut '{merek}' tapi domainnya BUKAN {domain_resmi}")
    if peringatan:
        hasil = f"WASPADA! Domain sebenarnya: {domain}\nLink ini mencurigakan:\n"
        for p in peringatan:
            hasil += "- " + p + "\n"
        return hasil + "Jangan login dan jangan isi data apa pun di sana."
    return f"Domain sebenarnya: {domain}\nTidak ada tanda bahaya yang dikenal. Tetap hati-hati: pemeriksaan ini membaca bentuk link, bukan menjamin isinya aman."

print("Bot Kasir Damian v4 berjalan. CTRL+C untuk berhenti.")

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
                balasan = "Halo! Saya bot Kasir Damian. Perintah: /kasir = catatan penjualan, /cuaca = cuaca Jakarta, /ceklink = periksa link mencurigakan. Contoh: /ceklink https://contoh-link.com"
            elif teks == "/kasir":
                balasan = "Catatan penjualan:\n" + open("penjualan.txt").read()
            elif teks == "/cuaca":
                balasan = ambil_cuaca()
            elif teks.startswith("/ceklink"):
                potongan = teks.split(" ", 1)
                if len(potongan) < 2:
                    balasan = "Caranya: ketik /ceklink lalu tempel linknya. Contoh: /ceklink https://facebook.com.login-gratis.xyz"
                else:
                    balasan = periksa_link(potongan[1].strip())
            else:
                balasan = "Anda menulis: " + teks
            requests.post(dasar + "/sendMessage", data={"chat_id": chat_id, "text": balasan}, timeout=15)
    except Exception as e:
        print("Koneksi bermasalah:", e)
        print("Mencoba lagi dalam 3 detik...")
        time.sleep(3)
    time.sleep(1)

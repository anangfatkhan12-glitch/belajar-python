import requests
import time

token = open("token.txt").read().strip()
dasar = f"https://api.telegram.org/bot{token}"
offset = 0
print("Bot Kasir Damian v2 berjalan. CTRL+C untuk berhenti.")

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
                balasan = "Halo! Saya bot Kasir Damian. Ketik /kasir untuk melihat catatan penjualan."
            elif teks == "/kasir":
                balasan = "Catatan penjualan:\n" + open("penjualan.txt").read()
            else:
                balasan = "Anda menulis: " + teks
            requests.post(dasar + "/sendMessage", data={"chat_id": chat_id, "text": balasan}, timeout=15)
    except Exception as e:
        print("Koneksi bermasalah:", e)
        print("Mencoba lagi dalam 3 detik...")
        time.sleep(3)
    time.sleep(1)

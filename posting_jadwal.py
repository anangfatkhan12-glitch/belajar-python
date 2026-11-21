import requests
import time
from datetime import datetime

token = open("token_fb.txt").read().strip()
page_id = "1513193645205371"

def posting_teks(pesan):
    hasil = requests.post(
        f"https://graph.facebook.com/v27.0/{page_id}/feed",
        data={"message": pesan, "access_token": token},
        timeout=15,
    ).json()
    if "id" in hasil:
        print("TERBIT:", pesan)
        return True
    print("GAGAL:", hasil["error"]["message"])
    return False

print("Alat posting terjadwal AKTIF. Tekan CTRL+C untuk berhenti.")
sudah = set()

while True:
    sekarang = datetime.now().strftime("%H:%M")
    tanggal = datetime.now().strftime("%Y-%m-%d")
    for baris in open("jadwal.txt").read().splitlines():
        if "|" not in baris:
            continue
        jam, pesan = baris.split("|", 1)
        kunci = tanggal + " " + jam.strip()
        if jam.strip() == sekarang and kunci not in sudah:
            if posting_teks(pesan.strip()):
                sudah.add(kunci)
    time.sleep(20)

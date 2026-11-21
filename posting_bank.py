import requests
import time
from datetime import datetime

token = open("token_fb.txt").read().strip()
page_id = "1513193645205371"
JAM_POSTING = ["04:00", "09:00", "19:00"]

def baca_baris(nama_file):
    try:
        return [b for b in open(nama_file).read().splitlines() if b.strip()]
    except FileNotFoundError:
        return []

def simpan_tambah(nama_file, teks):
    with open(nama_file, "a") as f:
        f.write(teks + "\n")

def ambil_dari_bank():
    terpakai = baca_baris("bank_terpakai.txt")
    for baris in baca_baris("bank_konten.txt"):
        nama, caption = baris.split("|", 1)
        if nama not in terpakai:
            return nama, caption
    open("bank_terpakai.txt", "w").close()
    for baris in baca_baris("bank_konten.txt"):
        nama, caption = baris.split("|", 1)
        return nama, caption
    return None, None

def posting_foto(nama, caption):
    try:
        with open("foto/" + nama, "rb") as berkas:
            hasil = requests.post(
                f"https://graph.facebook.com/v27.0/{page_id}/photos",
                files={"source": berkas},
                data={"caption": caption, "access_token": token},
                timeout=30,
            ).json()
    except Exception as e:
        print("Gangguan jaringan:", e)
        return False
    if "id" in hasil:
        print("TERBIT:", nama, "|", caption[:40])
        return True
    print("GAGAL:", hasil.get("error", {}).get("message"))
    return False

print("Bank putaran AKTIF. Jam posting:", ", ".join(JAM_POSTING))
print("Tekan CTRL+C untuk berhenti.")

while True:
    sekarang = datetime.now()
    tanggal = sekarang.strftime("%Y-%m-%d")
    jam_ini = sekarang.strftime("%H:%M")
    slot_terbit = baca_baris("slot_terbit.txt")
    for jam in JAM_POSTING:
        kunci = tanggal + " " + jam
        if jam <= jam_ini and kunci not in slot_terbit:
            nama, caption = ambil_dari_bank()
            if nama is None:
                print("Bank konten KOSONG - isi bank_konten.txt dulu")
                break
            if posting_foto(nama, caption):
                simpan_tambah("bank_terpakai.txt", nama)
                simpan_tambah("slot_terbit.txt", kunci)
    time.sleep(30)

import socket
from urllib.parse import urlparse

resmi = {"facebook": "facebook.com", "instagram": "instagram.com", "google": "google.com", "tokopedia": "tokopedia.com", "tiktok": "tiktok.com", "whatsapp": "whatsapp.com", "github": "github.com"}
pasaran = ["123456", "password", "qwerty", "12345678", "111111", "admin", "sayang", "indonesia"]

def periksa_link():
    link = input("Tempel link yang mau diperiksa: ")
    if "://" not in link:
        link = "https://" + link
    bagian = urlparse(link)
    domain = bagian.hostname or ""
    print("Domain sebenarnya:", domain)
    peringatan = []
    if bagian.scheme != "https":
        peringatan.append("Tidak memakai https (koneksi tidak terenkripsi)")
    if domain.replace(".", "").isdigit():
        peringatan.append("Domain berupa angka IP - situs resmi tidak login lewat alamat angka")
    for merek, domain_resmi in resmi.items():
        if merek in domain and domain != domain_resmi and not domain.endswith("." + domain_resmi):
            peringatan.append(f"Menyebut '{merek}' tapi domainnya BUKAN {domain_resmi}")
    if peringatan:
        print("WASPADA! Link ini mencurigakan:")
        for p in peringatan:
            print("-", p)
        print("Jangan login dan jangan isi data apa pun di sana.")
    else:
        print("Tidak ada tanda bahaya yang dikenal. Tetap hati-hati: pemeriksaan ini membaca bentuk link, bukan menjamin isinya aman.")

def nilai_sandi():
    sandi = input("Kata sandi yang mau dinilai: ")
    poin = 0
    catatan = []
    if len(sandi) >= 8:
        poin += 1
    else:
        catatan.append("Kurang panjang: minimal 8 karakter, lebih aman 12+")
    if len(sandi) >= 12:
        poin += 1
    if any(c.islower() for c in sandi) and any(c.isupper() for c in sandi):
        poin += 1
    else:
        catatan.append("Campurkan huruf kecil DAN huruf besar")
    if any(c.isdigit() for c in sandi):
        poin += 1
    else:
        catatan.append("Tambahkan angka")
    if any(not c.isalnum() for c in sandi):
        poin += 1
    else:
        catatan.append("Tambahkan simbol seperti # ! ? -")
    if sandi.lower() in pasaran:
        poin = 0
        catatan = ["Ini kata sandi PASARAN - paling pertama ditebak penyerang"]
    label = {0: "SANGAT LEMAH", 1: "SANGAT LEMAH", 2: "LEMAH", 3: "SEDANG", 4: "KUAT", 5: "SANGAT KUAT"}
    print("Nilai:", poin, "/ 5 -", label[poin])
    for c in catatan:
        print("-", c)

def cek_satu_port(host, port):
    try:
        s = socket.create_connection((host, port), timeout=5)
        print(host, "port", port, ": TERBUKA")
        s.close()
    except Exception as e:
        print(host, "port", port, ": TERTUTUP/TERBLOKIR -", e)

def periksa_jaringan():
    host = input("Nama situs (contoh: github.com): ").strip()
    try:
        ip = socket.gethostbyname(host)
        print("Alamat IP", host, "adalah", ip)
    except Exception as e:
        print("Nama situs tidak ditemukan:", e)
        return
    cek_satu_port(host, 443)
    cek_satu_port(host, 22)

while True:
    print()
    print("=== APLIKASI PELINDUNG DAMIAN ===")
    print("1. Cek link phishing")
    print("2. Cek kekuatan kata sandi")
    print("3. Cek DNS & port sebuah situs")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    if pilihan == "1":
        periksa_link()
    elif pilihan == "2":
        nilai_sandi()
    elif pilihan == "3":
        periksa_jaringan()
    elif pilihan == "4":
        print("Tetap waspada, tetap aman. Program ditutup.")
        break
    else:
        print("Pilihan tidak ada, coba lagi.")

import socket
import requests
from urllib.parse import urlparse, parse_qs

MEREK = {
    "facebook": "facebook.com",
    "instagram": "instagram.com",
    "whatsapp": "whatsapp.com",
    "google": "google.com",
    "tiktok": "tiktok.com",
}

SANDI_UMUM = ["password", "123456", "12345678", "qwerty", "admin123", "iloveyou"]

def periksa_link(url):
    alasan = []
    if not url.startswith("https://"):
        alasan.append("Tidak memakai https")
    domain = urlparse(url).netloc
    angka = domain.replace(".", "").replace(":", "")
    if angka.isdigit():
        alasan.append("Domain berupa alamat IP")
    for merek, resmi in MEREK.items():
        if merek in domain and domain != resmi and not domain.endswith("." + resmi):
            alasan.append("Memakai nama " + merek + " tapi bukan situs resmi " + resmi)
    return alasan

def nilai_sandi(sandi):
    if sandi.lower() in SANDI_UMUM:
        return 0
    skor = 0
    if len(sandi) >= 8:
        skor += 1
    if len(sandi) >= 12:
        skor += 1
    if any(c.islower() for c in sandi) and any(c.isupper() for c in sandi):
        skor += 1
    if any(c.isdigit() for c in sandi):
        skor += 1
    if any(not c.isalnum() for c in sandi):
        skor += 1
    return skor

def periksa_jaringan():
    situs = input("Nama situs (contoh: github.com): ")
    try:
        ip = socket.gethostbyname(situs)
        print("Alamat IP", situs, "adalah", ip)
        for port in [443, 22]:
            s = socket.socket()
            s.settimeout(3)
            hasil = s.connect_ex((situs, port))
            if hasil == 0:
                print(situs, "port", port, ": TERBUKA")
            else:
                print(situs, "port", port, ": tertutup")
            s.close()
    except:
        print("Situs tidak ditemukan. Cek ejaannya.")

def tembus_link():
    url = input("Tempel link yang mau ditembus: ")
    try:
        r = requests.get(url, timeout=15)
        print("Jumlah lompatan:", len(r.history))
        print("Alamat ASLI:", r.url)
        alasan = periksa_link(r.url)
        if alasan:
            print("Hasil periksa alamat asli: WASPADA")
            for a in alasan:
                print("-", a)
        else:
            print("Hasil periksa alamat asli: AMAN")
    except:
        print("Gagal menembus link. Cek koneksi atau alamatnya.")

def bedah_link():
    url = input("Tempel link panjangnya: ")
    p = urlparse(url)
    print("Skema  :", p.scheme)
    print("Domain :", p.netloc)
    print("Jalur  :", p.path)
    params = parse_qs(p.query)
    if params:
        print("Isi parameter:")
        for nama, nilai in params.items():
            isi = nilai[0]
            print("-", nama, "=", isi)
            if "http" in isi:
                print("  *** ADA ALAMAT BERSEMBUNYI:", isi)
                alasan = periksa_link(isi)
                if alasan:
                    print("  Hasil periksa alamat sembunyi: WASPADA")
                    for a in alasan:
                        print("  -", a)
                else:
                    print("  Hasil periksa alamat sembunyi: AMAN")
    else:
        print("Tidak ada parameter.")
    try:
        r = requests.get(url, timeout=15)
        print("Alamat AKHIR setelah diikuti:", r.url)
    except:
        print("Gagal mengikuti link sampai akhir.")

def panduan_pulihkan():
    print("=== PENOLONG PEMULIHAN AKUN ===")
    print("Alat ini memberi PANDUAN resmi, bukan membobol akun.")
    print()
    print("Platform yang bermasalah:")
    print("1. Instagram")
    platform = input("Pilih (1): ")
    if platform == "1":
        print()
        print("Apa yang masih bisa Anda akses?")
        print("1. Email terdaftar")
        print("2. Nomor HP terdaftar")
        print("3. Email dan nomor HP")
        print("4. Keduanya hilang")
        punya = input("Pilih (1/2/3/4): ")
        print()
        if punya == "1":
            print("JALUR EMAIL:")
            print("- Buka instagram.com/accounts/password/reset")
            print("- Masukkan email terdaftar; tautan atur ulang sandi dikirim ke email itu")
            print("- Buka emailnya, ketuk tautannya, buat sandi baru yang kuat")
        elif punya == "2":
            print("JALUR NOMOR HP:")
            print("- Di aplikasi Instagram: Lupa kata sandi? lalu masukkan nama pengguna")
            print("- Pilih kode lewat SMS atau WhatsApp ke nomor terdaftar")
            print("- Masukkan kodenya SENDIRI, jangan dibagikan ke siapa pun")
        elif punya == "3":
            print("JALUR PALING MUDAH:")
            print("- Pakai salah satu: tautan email atau kode SMS/WhatsApp")
            print("- Setelah masuk, segera perbarui email dan nomor di pengaturan akun")
        elif punya == "4":
            print("JALUR VERIFIKASI IDENTITAS:")
            print("- Di layar pemulihan pilih 'Tidak lagi memiliki akses ke sini?'")
            print("- Ikuti bantuan resmi di help.instagram.com atau instagram.com/hacked")
            print("- Siapkan email AKTIF untuk dihubungi Meta dan verifikasi video selfie")
            print("- Nomor hilang? Urus kartu pengganti nomor yang sama di gerai operator dengan KTP")
            print("- Prosesnya bisa beberapa hari; keputusan akhir di tangan Meta")
        else:
            print("Pilihan tidak dikenal.")
    else:
        print("Platform lain menyusul di versi berikutnya.")
    print()
    print("=== ATURAN AMAN UNTUK SEMUA AKUN ===")
    print("- Hanya percaya alamat resmi: instagram.com, help.instagram.com, facebook.com")
    print("- Kode dan tautan pemulihan TIDAK PERNAH dibagikan ke siapa pun")
    print("- Tidak ada jasa bobol/unban akun yang sah - yang menawarkan itu penipu")
    print("- Setelah pulih: aktifkan verifikasi dua langkah dan simpan sandi di tempat aman")

while True:
    print()
    print("=== APLIKASI PELINDUNG DAMIAN v4 ===")
    print("1. Cek link phishing")
    print("2. Cek kekuatan kata sandi")
    print("3. Cek DNS & port sebuah situs")
    print("4. Tembus link pendek")
    print("5. Bedah link panjang")
    print("6. Panduan pulihkan akun")
    print("7. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5/6/7): ")
    if pilihan == "1":
        url = input("Tempel link yang mencurigakan: ")
        alasan = periksa_link(url)
        if alasan:
            print("Hasil: WASPADA")
            for a in alasan:
                print("-", a)
        else:
            print("Hasil: AMAN")
    elif pilihan == "2":
        sandi = input("Kata sandi yang mau dinilai: ")
        skor = nilai_sandi(sandi)
        if skor <= 2:
            label = "LEMAH"
        elif skor == 3:
            label = "SEDANG"
        elif skor == 4:
            label = "KUAT"
        else:
            label = "SANGAT KUAT"
        print("Skor:", skor, "/5 -", label)
    elif pilihan == "3":
        periksa_jaringan()
    elif pilihan == "4":
        tembus_link()
    elif pilihan == "5":
        bedah_link()
    elif pilihan == "6":
        panduan_pulihkan()
    elif pilihan == "7":
        print("Tetap waspada, tetap aman. Program ditutup.")
        break
    else:
        print("Pilihan tidak dikenal.")

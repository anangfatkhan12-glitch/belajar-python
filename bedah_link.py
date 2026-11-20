import requests
from urllib.parse import urlparse, parse_qs

print("=== BEDAH LINK PANJANG ===")
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
else:
    print("Tidak ada parameter.")

try:
    r = requests.get(url, timeout=15)
    print("Alamat AKHIR setelah diikuti:", r.url)
except:
    print("Gagal mengikuti link sampai akhir.")

import requests

print("=== PENEMBUS LINK PENDEK ===")
url = input("Tempel link yang mau ditembus: ")

try:
    r = requests.get(url, timeout=15)
    print("Jumlah lompatan:", len(r.history))
    print("Alamat ASLI:")
    print(r.url)
except:
    print("Gagal menembus link. Cek koneksi atau alamatnya.")

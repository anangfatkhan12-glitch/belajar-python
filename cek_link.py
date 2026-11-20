from urllib.parse import urlparse

resmi = {"facebook": "facebook.com", "instagram": "instagram.com", "google": "google.com", "tokopedia": "tokopedia.com", "tiktok": "tiktok.com", "whatsapp": "whatsapp.com", "github": "github.com"}

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

print("--- HASIL ---")
if peringatan:
    print("WASPADA! Link ini mencurigakan:")
    for p in peringatan:
        print("-", p)
else:
    print("Tidak ada tanda bahaya yang dikenal. Tetap hati-hati: alat ini memeriksa bentuk link, bukan menjamin isinya aman.")

sandi = input("Kata sandi yang mau dinilai: ")

pasaran = ["123456", "password", "qwerty", "12345678", "111111", "admin", "sayang", "indonesia"]
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
if poin >= 4:
    print("Sandi seperti ini layak dipakai (dan jangan dipakai ulang di akun lain).")

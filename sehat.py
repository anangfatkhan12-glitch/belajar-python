import datetime

HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

MENU = [
    "Telur rebus + pisang | nasi, tempe, sayur bening bayam | tahu kukus + lalapan",
    "Roti gandum + telur | nasi, ikan kembung, tumis kangkung | sup sayur + telur",
    "Pisang + susu | nasi, ayam rebus, capcay | tempe + sayur asem",
    "Telur dadar sayur | nasi, tahu, sayur lodeh | ikan pepes + lalapan",
    "Bubur kacang hijau | nasi, ayam bakar, urap sayur | sup bening + tempe",
    "Nasi + telur balado | nasi, ikan goreng, lalapan + sambal tomat | soto ayam bening",
    "Roti + telur | nasi, daging sedikit, sayur singkong | pepaya + tahu kukus",
]

AKTIVITAS = [
    "Jalan kaki cepat 30 menit + push-up 3 x 10",
    "Peregangan 10 menit + squat 3 x 12",
    "Jalan kaki 30 menit + plank 3 x 30 detik",
    "Istirahat aktif: jalan santai 15 menit + peregangan",
    "Joging ringan 20 menit",
    "Olahraga bebas 45 menit: bersepeda, berenang, atau futsal",
    "Istirahat total: pulihkan badan, siapkan minggu depan",
]

def tampil_jam(jam):
    jam = jam % 24
    j = int(jam)
    m = int(round((jam - j) * 60))
    if m == 60:
        j = (j + 1) % 24
        m = 0
    return f"{j:02d}:{m:02d}"

hari_ini = datetime.date.today().weekday()

print("=== ASISTEN SEHAT DAMIAN ===")
print("Hari ini:", HARI[hari_ini])
print()

bangun = float(input("Besok mau bangun jam berapa? (contoh 5 atau 5.5): "))
print()
print("PILIHAN JAM TIDUR MALAM INI:")
print("- Tidur 9 jam (6 siklus, paling segar): tidur pukul", tampil_jam(bangun - 9))
print("- Tidur 7,5 jam (5 siklus, cukup): tidur pukul", tampil_jam(bangun - 7.5))
print("Tidur dalam kelipatan siklus 90 menit membuat bangun lebih segar.")
print()

berat = float(input("Berat badan Anda (kg): "))
air_ml = berat * 35
print("Kebutuhan air hari ini sekitar:", int(air_ml), "ml =", round(air_ml / 1000, 1), "liter")
print()

print("MENU SEHAT HARI INI (sarapan | siang | malam):")
print(MENU[hari_ini])
print()
print("AKTIVITAS HARI INI:")
print(AKTIVITAS[hari_ini])
print()
print("Saran umum untuk kebugaran, bukan nasihat medis.")

import datetime
import requests

HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

MENU = [
    "Telur rebus + pisang | nasi, tempe goreng, sayur bening bayam | tahu kukus + lalapan",
    "Roti tawar + telur ceplok | nasi, ikan kembung goreng, tumis kangkung | sup sayur sederhana",
    "Pisang + segelas susu | nasi, ayam rebus, capcay sederhana | tempe bacem + sayur asem",
    "Telur dadar sayur | nasi, tahu goreng, sayur lodeh | ikan asin + lalapan + sambal",
    "Bubur kacang hijau | nasi, ayam bakar, urap sayur | sup bening + tempe goreng",
    "Nasi + telur balado | nasi, ikan goreng, lalapan + sambal tomat | soto ayam bening",
    "Roti + telur | nasi, sayur singkong + ikan asin | pepaya + tahu kukus",
]

MINUMAN = [
    "Air putih + teh tawar hangat",
    "Air jahe hangat (jahe geprek + air panas)",
    "Air putih dengan perasan jeruk nipis",
    "Es teh tawar buatan sendiri",
    "Air kelapa atau air putih dingin setelah berolahraga",
    "Kopi hitam tanpa gula (pagi saja, jangan malam)",
    "Jamu kunyit asam buatan sendiri atau air putih hangat",
]

OLAHRAGA = [
    "FOKUS: dada dan lengan\n- Pemanasan: jalan di tempat 2 menit\n- Push-up 3 x 10\n- Plank 3 x 30 detik\n- Pendinginan: peregangan tangan dan dada 3 menit",
    "FOKUS: kaki\n- Pemanasan: jalan di tempat 2 menit\n- Squat 3 x 12\n- Calf raise (jinjit) 3 x 15\n- Wall sit 3 x 30 detik\n- Jalan kaki santai 10 menit",
    "FOKUS: kardio ringan\n- Jalan cepat 30 menit\n- Peregangan seluruh badan 10 menit",
    "FOKUS: perut dan inti\n- Crunch 3 x 12\n- Leg raise 3 x 10\n- Plank 3 x 40 detik\n- Mountain climber 3 x 20",
    "FOKUS: ringan (hari ibadah)\n- Joging ringan 20 menit\n- Peregangan 5 menit\nSaran waktu: setelah Subuh atau sebelum Maghrib",
    "FOKUS: seluruh badan\n- Jumping jack 3 x 30\n- Push-up 3 x 10\n- Squat 3 x 12\n- Plank 3 x 30 detik",
    "ISTIRAHAT TOTAL\n- Jalan santai bersama keluarga 15-30 menit\n- Tidur cukup, siapkan minggu depan",
]

SHALAT_CADANGAN = {
    "Subuh": "04:00",
    "Dzuhur": "11:35",
    "Ashar": "15:00",
    "Maghrib": "17:45",
    "Isya": "19:00",
}

def tampil_jam(jam):
    jam = jam % 24
    j = int(jam)
    m = int(round((jam - j) * 60))
    if m == 60:
        j = (j + 1) % 24
        m = 0
    return f"{j:02d}:{m:02d}"

def jadwal_shalat():
    try:
        url = "https://api.aladhan.com/v1/timingsByCity?city=Banyumas&country=Indonesia&method=20"
        data = requests.get(url, timeout=15).json()
        t = data["data"]["timings"]
        print("JADWAL SHALAT HARI INI (Banyumas, dari internet):")
        print("- Subuh  :", t["Fajr"][:5])
        print("- Dzuhur :", t["Dhuhr"][:5])
        print("- Ashar  :", t["Asr"][:5])
        print("- Maghrib:", t["Maghrib"][:5])
        print("- Isya   :", t["Isha"][:5])
    except:
        print("JADWAL SHALAT HARI INI (perkiraan - jaringan gagal):")
        for nama, jam in SHALAT_CADANGAN.items():
            print("-", nama, ":", jam)

hari_ini = datetime.date.today().weekday()

print("=== ASISTEN SEHAT DAMIAN v2 ===")
print("Hari ini:", HARI[hari_ini])
print()
jadwal_shalat()
print()

bangun = float(input("Besok mau bangun jam berapa? (contoh 5 atau 5.5): "))
print()
print("PILIHAN JAM TIDUR MALAM INI:")
print("- Tidur 9 jam (6 siklus, paling segar): tidur pukul", tampil_jam(bangun - 9))
print("- Tidur 7,5 jam (5 siklus, cukup): tidur pukul", tampil_jam(bangun - 7.5))
print("Catatan: bangun sebelum Subuh memberi waktu tenang untuk ibadah.")
print()

berat = float(input("Berat badan Anda (kg): "))
air_ml = berat * 35
print("Kebutuhan air hari ini sekitar:", int(air_ml), "ml =", round(air_ml / 1000, 1), "liter")
print()

print("MENU HEMAT HARI INI (sarapan | siang | malam):")
print(MENU[hari_ini])
print("MINUMAN HEMAT HARI INI:")
print(MINUMAN[hari_ini])
print()
print("OLAHRAGA HARI INI:")
print(OLAHRAGA[hari_ini])
print()
print("Saran umum untuk kebugaran, bukan nasihat medis.")

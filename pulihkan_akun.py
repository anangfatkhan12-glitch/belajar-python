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

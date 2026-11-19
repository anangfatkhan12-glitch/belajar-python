barang = []

while True:
    print("=== KASIR SEDERHANA ===")
    print("1. Tambah barang")
    print("2. Lihat daftar dan total")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        nama = input("Nama barang: ")
        harga = int(input("Harga: "))
        jumlah = int(input("Jumlah: "))
        barang.append({"nama": nama, "harga": harga, "jumlah": jumlah})
        print("Barang ditambahkan.")
        file = open("penjualan.txt", "a")
        file.write(nama + " - Rp " + str(harga * jumlah) + "\n")
        file.close()
        print("Tersimpan ke penjualan.txt")
    elif pilihan == "2":
        total = 0
        for b in barang:
            subtotal = b["harga"] * b["jumlah"]
            total = total + subtotal
            print(b["nama"], "x", b["jumlah"], "= Rp", subtotal)
        print("TOTAL: Rp", total)
    elif pilihan == "3":
        print("Terima kasih. Program kasir ditutup.")
        break
    else:
        print("Pilihan tidak ada, coba lagi.")


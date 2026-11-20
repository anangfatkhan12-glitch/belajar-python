class Barang:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def subtotal(self):
        return self.harga * self.jumlah

class Kasir:
    def __init__(self):
        self.daftar = []

    def tambah(self, barang):
        self.daftar.append(barang)

    def total(self):
        t = 0
        for b in self.daftar:
            t = t + b.subtotal()
        return t

    def tampilkan(self):
        for b in self.daftar:
            print(b.nama, "x", b.jumlah, "= Rp", b.subtotal())
        print("TOTAL: Rp", self.total())

    def simpan(self):
        file = open("penjualan_oop.txt", "w")
        for b in self.daftar:
            file.write(b.nama + " - Rp " + str(b.subtotal()) + "\n")
        file.write("TOTAL: Rp " + str(self.total()) + "\n")
        file.close()

k = Kasir()
while True:
    print("=== KASIR OOP ===")
    print("1. Tambah barang")
    print("2. Lihat daftar dan total")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")
    if pilihan == "1":
        nama = input("Nama barang: ")
        harga = int(input("Harga: "))
        jumlah = int(input("Jumlah: "))
        k.tambah(Barang(nama, harga, jumlah))
        k.simpan()
        print("Barang ditambahkan dan tersimpan.")
    elif pilihan == "2":
        k.tampilkan()
    elif pilihan == "3":
        print("Terima kasih. Program kasir ditutup.")
        break
    else:
        print("Pilihan tidak ada, coba lagi.")

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

k = Kasir()
k.tambah(Barang("beras", 10000, 2))
k.tambah(Barang("minyak", 15000, 1))
k.tampilkan()

class Barang:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def subtotal(self):
        return self.harga * self.jumlah

b1 = Barang("beras", 10000, 2)
b2 = Barang("minyak", 15000, 1)
print(b1.nama, "subtotal:", b1.subtotal())
print(b2.nama, "subtotal:", b2.subtotal())
print("TOTAL:", b1.subtotal() + b2.subtotal())

angka1 = int(input("Angka pertama: "))
angka2 = int(input("Angka kedua: "))
operasi = input("Pilih operasi (+, -, *, /): ")

if operasi == "+":
    print("Hasil:", angka1 + angka2)
elif operasi == "-":
    print("Hasil:", angka1 - angka2)
elif operasi == "*":
    print("Hasil:", angka1 * angka2)
elif operasi == "/":
    print("Hasil:", angka1 / angka2)
else:
    print("Operasi tidak dikenal")

file = open("catatan.txt", "w")
file.write("While loop berhasil. Saya terus belajar.")
file.close()

file = open("catatan.txt", "r")
isi = file.read()
file.close()

print("Isi catatan Anda:")
print(isi)

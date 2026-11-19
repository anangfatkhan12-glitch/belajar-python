import re
teks = open("token_mentah.txt").read()
token = re.search(r"\d+:[A-Za-z0-9_-]{30,}", teks).group(0)
open("token.txt", "w").write(token)
print("Token tersimpan. Panjang token:", len(token))


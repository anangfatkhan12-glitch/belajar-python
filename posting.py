import requests

token = open("token_fb.txt").read().strip()
page_id = "1513193645205371"

pesan = "Halo semuanya! Ini postingan tes pertama dari alat Termux saya."

hasil = requests.post(
    f"https://graph.facebook.com/v27.0/{page_id}/feed",
    data={"message": pesan, "access_token": token},
    timeout=15,
).json()

if "id" in hasil:
    print("BERHASIL! Postingan terbit, ID:", hasil["id"])
else:
    print("GAGAL:", hasil["error"]["message"])

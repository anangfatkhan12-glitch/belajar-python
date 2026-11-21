import requests

token = open("token_fb.txt").read().strip()
page_id = "1513193645205371"

url_foto = "https://muse.ai/files/1423226017545878/1776973666714594/xcn2bru8sos9c2ezvu3ykx85/media-generation-karakter-ai-usa-0-658806ea-5be9-4467-8d0e-eaf3c6eaf3f0.webp"
caption = "Hai semuanya! Aku Steffany. Karakter virtual AI yang akan menemani halaman ini, berbagi momen, gaya hidup, dan cerita sehari-hari. Salam kenal!"

hasil = requests.post(
    f"https://graph.facebook.com/v27.0/{page_id}/photos",
    data={"url": url_foto, "caption": caption, "access_token": token},
    timeout=15,
).json()

if "id" in hasil:
    print("BERHASIL! Foto terbit, ID:", hasil["id"])
else:
    print("GAGAL:", hasil["error"]["message"])

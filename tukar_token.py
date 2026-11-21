import requests

token_user = open("token_user.txt").read().strip()
id_app = open("id_app.txt").read().strip()
rahasia = open("rahasia_app.txt").read().strip()

# Langkah 1: tukar token pendek menjadi token jangka panjang
tukar = requests.get(
    "https://graph.facebook.com/v27.0/oauth/access_token",
    params={
        "grant_type": "fb_exchange_token",
        "client_id": id_app,
        "client_secret": rahasia,
        "fb_exchange_token": token_user,
    },
    timeout=15,
).json()

if "access_token" not in tukar:
    print("Tukar token GAGAL:", tukar["error"]["message"])
    raise SystemExit

token_panjang = tukar["access_token"]
print("Token jangka panjang OK:", len(token_panjang), "karakter")

# Langkah 2: ambil token Page steffany ter
hasil = requests.get(
    "https://graph.facebook.com/v27.0/me/accounts",
    params={"access_token": token_panjang},
    timeout=15,
).json()

for page in hasil["data"]:
    print("Page:", page["name"], "| ID:", page["id"])
    if page["id"] == "1513193645205371":
        with open("token_fb.txt", "w") as f:
            f.write(page["access_token"])
        print("Token Page tersimpan di token_fb.txt:", len(page["access_token"]), "karakter")

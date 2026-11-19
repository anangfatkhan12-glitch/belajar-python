import requests
token = open("token.txt").read().strip()
url = f"https://api.telegram.org/bot{token}/getUpdates"
data = requests.get(url).json()
pesan = data["result"][-1]["message"]
print("Chat ID Anda:", pesan["chat"]["id"])
print("Dari:", pesan["chat"]["first_name"])
print("Isi pesan:", pesan["text"])

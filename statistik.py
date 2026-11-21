import requests

token = open("token_fb.txt").read().strip()
page_id = "1513193645205371"
dasar = f"https://graph.facebook.com/v27.0/{page_id}"

info = requests.get(
    dasar,
    params={"fields": "name,fan_count,followers_count", "access_token": token},
    timeout=15,
).json()

if "error" in info:
    print("GAGAL:", info["error"]["message"])
    raise SystemExit

print("=== STATISTIK PAGE ===")
print("Nama     :", info.get("name"))
print("Pengikut :", info.get("followers_count", 0))

posts = requests.get(
    dasar + "/published_posts",
    params={"fields": "message,created_time", "limit": 5, "access_token": token},
    timeout=15,
).json()

if "error" in posts:
    print("GAGAL:", posts["error"]["message"])
    raise SystemExit

print()
print("=== 5 POSTINGAN TERBARU ===")
for p in posts.get("data", []):
    pesan = p.get("message", "(postingan tanpa teks)")
    if len(pesan) > 50:
        pesan = pesan[:50] + "..."
    print("-", p.get("created_time", "")[:10], "|", pesan)

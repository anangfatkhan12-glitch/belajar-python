import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=-6.2&longitude=106.8&current=temperature_2m,weather_code,wind_speed_10m"
try:
    data = requests.get(url, timeout=15).json()
    print(data["current"])
except Exception as e:
    print("Gagal mengambil data:", e)

import socket

def cek(host, port):
    try:
        s = socket.create_connection((host, port), timeout=5)
        print(host, "port", port, ": TERBUKA")
        s.close()
    except Exception as e:
        print(host, "port", port, ": TERTUTUP/TERBLOKIR -", e)

cek("github.com", 443)
cek("github.com", 22)
cek("api.telegram.org", 443)

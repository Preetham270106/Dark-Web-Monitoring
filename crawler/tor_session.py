import requests

def get_tor_session():
    session = requests.Session()
    session.proxies = {
        "http": "socks5h://127.0.0.1:9050",
        "https": "socks5h://127.0.0.1:9050"
    }
    session.headers.update({
        "User-Agent": "Mozilla/5.0"
    })
    return session
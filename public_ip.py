import urllib.request

def show_public_ip():
    ip = urllib.request.urlopen(
        "https://api.ipify.org",
        timeout=5
    ).read().decode("utf-8")

    print("Your Public IP:", ip)

show_public_ip()

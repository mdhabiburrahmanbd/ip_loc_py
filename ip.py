import socket
import urllib.request

def local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def public_ip():
    response = urllib.request.urlopen(
        "https://api.ipify.org",
        timeout=5
    )
    return response.read().decode("utf-8")

def main():
    print("Local IP:", local_ip())
    print("Public IP:", public_ip())

main()

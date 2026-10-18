import socket

def show_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("Your IP Address:", ip_address)

show_ip()

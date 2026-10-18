import socket
import struct

def get_public_ip():
    server = ("stun.l.google.com", 19302)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)

    try:
        request = (
            b"\x00\x01\x00\x00"
            + b"\x21\x12\xa4\x42"
            + b"123456789012"
        )

        sock.sendto(request, server)
        response, _ = sock.recvfrom(2048)

        pos = 20

        while pos + 4 <= len(response):
            attr_type, length = struct.unpack(
                "!HH", response[pos:pos + 4]
            )

            value = response[pos + 4:pos + 4 + length]

            if attr_type == 0x0020 and length >= 8:
                ip_bytes = bytes(
                    value[i] ^ b"\x21\x12\xa4\x42"[i - 4]
                    for i in range(4, 8)
                )

                return socket.inet_ntoa(ip_bytes)

            pos += 4 + ((length + 3) // 4) * 4

        return "Public IP not found"

    finally:
        sock.close()


def main():
    print("Your Public IP:", get_public_ip())


if __name__ == "__main__":
    main()

import socket
import threading

target = input("Enter target: ")
print(f"\nScanning {target}...\n")

services = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        service = services.get(port, "Unknown")

        try:
            if port in [80, 8080]:
                s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode())

            banner = s.recv(1024)
            response = banner.decode(errors='ignore')

            output = f"[OPEN] {port} → {service}"

            # Extract HTTP info
            if "HTTP" in response:
                first_line = response.split("\n")[0]
                output += f" | {first_line}"

                for line in response.split("\n"):
                    if "Location:" in line:
                        output += f" | {line.strip()}"

            print(output)

        except:
            print(f"[OPEN] {port} → {service} | No banner")

    s.close()

threads = []

for port in range(20, 101):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
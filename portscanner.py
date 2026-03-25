import socket
import threading
import time

target = input("Enter target: ")
start = int(input("Enter start port: "))
end = int(input("Enter end port: "))

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

lock = threading.Lock()

# Clear file
open("results.txt", "w").close()

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        service = services.get(port, "Unknown")
        output = f"[OPEN] {port} → {service}"

        try:
            if port in [80, 8080]:
                s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode())

            # 🔥 Proper receive loop
            data = b""
            while True:
                try:
                    chunk = s.recv(1024)
                    if not chunk:
                        break
                    data += chunk
                except:
                    break

            response = data.decode(errors='ignore')

            if "HTTP" in response:
                lines = response.split("\r\n")

                if len(lines) > 0:
                    output += f" | {lines[0]}"

                for line in lines:
                    if line.startswith("Location:"):
                        output += f" | {line}"

        except:
            output += " | No banner"

        print(output)

        # 🔥 FIXED encoding
        with lock:
            with open("results.txt", "a", encoding="utf-8") as f:
                f.write(output + "\n")

    s.close()

start_time = time.time()

threads = []

for port in range(start, end + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()

print(f"\nScan completed in {end_time - start_time:.2f} seconds")
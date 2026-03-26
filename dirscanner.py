import requests
import threading
import time

base_url = "http://127.0.0.1:5000"

lock = threading.Lock()

def scan(directory):
    url = f"{base_url}/{directory}"

    try:
        response = requests.get(url)

        if response.status_code in [200, 301, 403]:
            output = f"[FOUND] {url} → {response.status_code}"

            print(output)

            with lock:
                with open("dir_results.txt", "a", encoding="utf-8") as f:
                    f.write(output + "\n")

    except:
        pass


# clear file
open("dir_results.txt", "w").close()

threads = []

with open("dir.txt", "r") as file:
    for line in file:
        directory = line.strip()

        t = threading.Thread(target=scan, args=(directory,))
        threads.append(t)
        t.start()

        time.sleep(0.05)  # small delay (stealth)

for t in threads:
    t.join()

print("\nScan completed.")
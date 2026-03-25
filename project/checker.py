import time

def check_password(target):
    attempts = 0
    start_time = time.time()
    target = target.lower().strip()

    try:
        with open("wordlist.txt", "r") as file:
            for line in file:
                password = line.strip()

                if not password:
                    continue

                attempts += 1

                if password.lower() == target:
                    end_time = time.time()
                    return f"FOUND in {attempts} attempts | Time: {end_time - start_time:.4f}s"

        end_time = time.time()
        return f"NOT FOUND after {attempts} attempts | Time: {end_time - start_time:.4f}s"

    except FileNotFoundError:
        return "wordlist.txt file not found"
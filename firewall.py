import random
def main():
    firewall_rules = {
        "192.168.1.1" : "block",
        "192.168.1.4" : "block",
        "192.168.1.9" : "block",
        "192.168.1.13" : "block",
        "192.168.1.16" : "block",
        "192.168.1.19" : "block"
    }

    for i in range(12):
        ip_address = 
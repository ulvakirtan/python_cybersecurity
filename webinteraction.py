import requests

url=input("Enter the URL to fetch: ")

response=requests.get(url)

print("Status Code:",response.status_code)
print("Headers:",response.headers)
print("Content:",response.text[:200])
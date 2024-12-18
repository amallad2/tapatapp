import datetime
import secrets
import string
import requests

def provaFunc():
    return "PROVA FUNC"



# Define the URL and data payload
url = "http://localhost:5000/provapost"
data = {
    "username": "value1",
    "key2": "value2",
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

# Send the POST request
response = requests.post(url, data=data, headers=headers)

# Print the response
print("Status Code:", response.status_code)
print("Response Body:", response.text)



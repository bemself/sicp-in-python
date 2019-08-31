import requests

token="5rZ5xPpKhXd3YBqZ3m_z"
url = f"https://gitlab.com/api/v4/users?private_token={token}"

data = {
    'name': 'vivian',
    'username': 'vivian',
    'email':'wanjiagulumi@outlook.com',
     'password':'debuguself'
}

headers = {
    'Content-type':'application/json'
}
resp = requests.post(url, headers=headers, json=data)
# resp = requests.get(url + "&order_by=id")
print(resp.text)
print(resp.status_code)
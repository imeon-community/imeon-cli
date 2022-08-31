import requests
session = requests.Session()


url_login = "http://10.0.20.201/login"
url_set = "http://10.0.20.201/toRedis"

payload = {'do_login': 'true',
           'email': 'installer@local',
           'passwd': 'Installer_P4SS'}

r = session.request("POST", url_login, data=payload)

print(f"Status Code: {r.status_code}, Response: {r.json()}")

r = session.request("POST", url_set, data={
    'inputdata': 'MODESMG'})

print(f"Status Code: {r.status_code}")

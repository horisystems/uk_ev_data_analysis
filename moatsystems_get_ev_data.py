import requests
import json

headers = {
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'username': 'evplug_user',
    'password': 'evplug_pass',
}

postToken = requests.post('https://evplugs.co/v1/token', headers=headers, json=json_data)
bearerToken = postToken.json().get('Document')
print(bearerToken)

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {bearerToken}'
}

uk_data = requests.get('https://evplugs.co/v1/uk', headers=headers)
uk_data_dict = uk_data.json().get('Document')
with open('./data/moatsystems_ev_charging_station.json', 'w') as fp: 
    json.dump(uk_data_dict, fp)

import json
import requests

from helpers import get_path_to_raw_data

base_url = 'http://ergast.com/api/f1/'
endpoint = 	'current/last/results.json'

response = requests.get(
	url=base_url + endpoint
)

data = response.json()

raw_data_path = get_path_to_raw_data()
raw_data_path.mkdir(parents=True, exist_ok=True)

with open(raw_data_path / 'current.json', 'w') as f:
	json.dump(data, f)
import json
import pandas as pd

from helpers import get_path_to_raw_data, get_path_to_tidy_data

tidy_data_path = get_path_to_tidy_data()
tidy_data_path.mkdir(parents=True, exist_ok=True)

with open(get_path_to_raw_data() / 'current.json', 'r') as f:
	d = json.load(f)

df = pd.json_normalize(d['MRData']['RaceTable']['Races'][0]['Results'])

df.to_parquet(tidy_data_path / 'current_race.parquet')
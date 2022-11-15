from pathlib import Path

def get_path_to_data():
    return Path('Data/')

def get_path_to_raw_data():
    return get_path_to_data() / 'RawData'

def get_path_to_tidy_data():
    return get_path_to_data() / 'TidyData'
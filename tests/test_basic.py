# -*- coding: utf-8 -*-

from sample.helpers import get_path_to_tidy_data
import pandas as pd

def test_check_dataframe_size():
    df = pd.read_parquet(get_path_to_tidy_data() / 'current_race.parquet')
    assert df.shape[1] == 26
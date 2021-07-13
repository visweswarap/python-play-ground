import uuid

import pandas as pd


def csv_to_parquet():

    df = pd.read_csv('../data/test.csv')
    print(df)
    # df.columns
    df.to_parquet('../data/test.parquet', compression='UNCOMPRESSED')  # compression="GZIP"


csv_to_parquet()

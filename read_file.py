import pandas as pd

def read_tsv(filepath, **kwargs):
    try:
        df = pd.read_csv(filepath, sep='\t', **kwargs)
        return df
    except Exception as e:
        print(f"Error reading the TSV file: {e}")
        return None
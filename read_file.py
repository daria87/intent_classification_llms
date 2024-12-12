import pandas as pd

def read_tsv(filepath, **kwargs):
    try:
        df = pd.read_csv(filepath, sep='\t', **kwargs)
        return df
    except Exception as e:
        print(f"Error reading the TSV file: {e}")
        return None

def write_tsv(df, file_path, encoding='utf-8', index=False):
    try:
        # Write the DataFrame to a TSV file
        df.to_csv(file_path, sep='\t', encoding=encoding, index=index)
        print(f"Data written to {file_path}")
    except Exception as e:
        print(f"Error writing to the file: {e}")
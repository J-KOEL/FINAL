import pandas as pd

def load_mapping(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df = df.dropna(how='all', axis=1)
    df = df.dropna(how='all')
    return dict(zip(df['Label'].str.strip(), df['Code'].astype(str).str.strip()))


import pandas as pd

def clean_csv(file_stream):
    df = pd.read_csv(file_stream)

    df.drop_duplicates(inplace=True)

    rows_with_missing_values = df.isna().any(axis=1).sum()
    if rows_with_missing_values/len(df) < 0.03:
        df.dropna(inplace=True)

    
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    string_cols = df.select_dtypes(exclude=['number']).columns
    df[string_cols] = df[string_cols].fillna("Brak_danych")
    return df
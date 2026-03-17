import pandas as pd

def analyze_csv(file_stream):

    df = pd.read_csv(file_stream)
    total_missing = int(df.isna().sum().sum())
    total_duplicates = int(df.duplicated().sum())

    return {
        "wymiary_tabeli": df.shape,
        "nazwy_kolumn": list(df.columns),
        "brakujace_wartosci": total_missing,
        "zduplikowane_wiersze": total_duplicates
    }

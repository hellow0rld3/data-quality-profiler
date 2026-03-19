import pandas as pd

def analyze_csv(df):
    total_missing = int(df.isna().sum().sum())
    missing_per_column = df.isna().sum().to_dict()
    missing_per_column = {col: int(val) for col, val in missing_per_column.items()}
    total_duplicates = int(df.duplicated().sum())
    types_per_column = df.dtypes.astype(str).to_dict()

    return {
        "wymiary_tabeli": df.shape,
        "nazwy_kolumn": list(df.columns),
        "brakujace_wartosci": total_missing,
        "zduplikowane_wiersze": total_duplicates,
        "braki w kolumnach" : missing_per_column,
        "typy kolumn" : types_per_column
    }

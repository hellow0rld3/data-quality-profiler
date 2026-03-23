import pandas as pd

def analyze_csv(df):
    score = 100
    total_missing = int(df.isna().sum().sum())
    missing_per_column = df.isna().sum().to_dict()
    missing_per_column = {col: int(val) for col, val in missing_per_column.items()}
    rows_with_missing_values = int(df.isna().any(axis=1).sum())
    total_duplicates = int(df.duplicated().sum())
    types_per_column = df.dtypes.astype(str).to_dict()

    total_cells = df.shape[0] * df.shape[1]
    total_rows = len(df)

    if total_cells == 0 or total_rows == 0:
        score = 0
    else:
        missing_percentage = (total_missing / total_cells) * 100
        duplicates_percentage = (total_duplicates / total_rows) * 100

        score -= (missing_percentage * 2)
        score -= (duplicates_percentage * 1)
        score = max(0, round(score, 2))


    return {
        "wymiary_tabeli": df.shape,
        "nazwy_kolumn": list(df.columns),
        "brakujace_wartosci": total_missing,
        "zduplikowane_wiersze": total_duplicates,
        "braki_w_kolumnach" : missing_per_column,
        "uszkodzone_wiersze" : rows_with_missing_values,
        "typy_kolumn" : types_per_column,
        "ocena_pliku" : score
    }



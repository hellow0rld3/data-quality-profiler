import pandas as pd

def clean_csv(df):
    #drop all the duplicates
    df.drop_duplicates(inplace=True)

    #dropping all the rows with missing values if theres less then 3%
    # of them in the entire dataset
    rows_with_missing_values = df.isna().any(axis=1).sum()
    if rows_with_missing_values/len(df) < 0.03:
        df.dropna(inplace=True)

    # filling in all the NaN values that remained as 0
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    string_cols = df.select_dtypes(exclude=['number']).columns


    #checking if the datatype for potentially numerical column is right,
    # because some or maybe even all values could mistakenly be given as string
    for col in string_cols:
        converted = pd.to_numeric(df[col], errors='coerce')

        if converted.notna().sum() > (len(df) * 0.5):
            df[col] = converted

    df[string_cols] = df[string_cols].fillna("Brak_danych")
    return df
import pandas as pd

def clean_csv(df, analysis_results):
    # drop all the duplicates
    df.drop_duplicates(inplace=True)

    # dropping all the rows with missing values if theres less then 3%
    # of them in the entire dataset
    rows_with_missing_values = analysis_results.get("uszkodzone wiersze", 0) 
    if len(df) > 0 and (rows_with_missing_values / len(df)) < 0.03:
        df.dropna(inplace=True)

    # checking if the datatype for potentially numerical column is right
    string_cols = df.select_dtypes(exclude=['number']).columns
    for col in string_cols:
        converted = pd.to_numeric(df[col], errors='coerce')

        if converted.notna().sum() > (len(df) * 0.5):
            df[col] = converted

    # Smart Imputer
    numeric_cols = df.select_dtypes(include=['number']).columns
    
    for col in numeric_cols:
        # For safety, if the column is completely empty, we fill with zeros
        if df[col].isna().all():
            df[col] = df[col].fillna(0)
            continue
            
        # Calculating mean and std for each column
        mean_val = df[col].mean()
        std_val = df[col].std()
        
        # If std is lower than mean (data is pretty stable), we fill with mean 
        if pd.notna(std_val) and std_val < abs(mean_val):
            df[col] = df[col].fillna(mean_val)
        else:
            # otherwise (data is distributed across wide range) we fill with median
            df[col] = df[col].fillna(df[col].median())

    # Filling the rest (real text)
    final_string_cols = df.select_dtypes(exclude=['number']).columns
    df[final_string_cols] = df[final_string_cols].fillna("Brak_danych")
    
    return df
import pandas as pd
import numpy as np

df = pd.read_csv("hospital_patient_management.csv")

df.drop_duplicates(inplace=True)

numeric_cols = df.select_dtypes(include=[np.number]).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())
    
text_cols = df.select_dtypes(include=["object", "string"]).columns

for col in text_cols:
    df[col] = df[col].astype(str)

    df[col] = df[col].str.strip()

    df[col] = df[col].str.lower()

    df[col] = df[col].replace(["", "nan", "none", "null"],np.nan)

    if col == "Patient_Name":
        df[col] = df[col].fillna("Unknown")
        
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

    df[col] = df[col].str.title()

for col in numeric_cols:
    df.loc[df[col] < 0, col] = df[col].median()

    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    median_value = df[col].median()

    df.loc[(df[col] < lower) | (df[col] > upper),col] = median_value

df.to_csv("hospital_patient_management_cleaned.csv",index=False)

print("Dataset cleaned successfully!")
print(df.head())
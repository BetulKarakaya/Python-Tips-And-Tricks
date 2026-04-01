import pandas as pd
import numpy as np

def clean_data(df):
    """Lowercases column names and removes spaces."""
    df.columns = [c.lower().replace(' ', '_') for c in df.columns]
    return df

def clip_outliers(df, column, lower=0.05, upper=0.95):
    """Clips extreme values in a specific column."""
    q_lower = df[column].quantile(lower)
    q_upper = df[column].quantile(upper)
    df[column] = df[column].clip(lower=q_lower, upper=q_upper)
    return df

def add_new_metric(df):
    """Adds a calculated new column."""
    df['performance_score'] = df['revenue'] / (df['age'] + 1)
    return df

def main():
    df = pd.DataFrame({
        'AGE': [25, 30, 45, 120, 22], # 120 is an outlier
        'REVENUE': [5000, 7000, 12000, 8000, 4500]
    })

    # TRICK: Chaining with Pipe 
    df_final = (df
                .pipe(clean_data)\
                .pipe(clip_outliers, column='age')\
                .pipe(add_new_metric)
            )

    print(df_final)


if __name__ == "__main__":
    main()
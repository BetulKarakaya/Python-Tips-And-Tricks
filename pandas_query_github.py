import pandas as pd

def main():
    df = pd.DataFrame({
        'city': ['Ankara', 'Istanbul', 'Izmir', 'Bursa', 'Antalya'],
        'sales_volume': [150, 450, 300, 200, 500],
        'is_in_stock': [True, True, False, True, False]
    })

    # Define an external variable
    min_sales_threshold = 250

    # Note: Use the '@' symbol to reference variables from your local environment
    filtered_df = df.query("sales_volume > @min_sales_threshold and is_in_stock == True")

    print(filtered_df)


if __name__ == "__main__":
    main()
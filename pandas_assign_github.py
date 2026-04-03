import pandas as pd
import numpy as np

def main():
    # Sample Dataset (Product sales)
    df = pd.DataFrame({
        'product_name': ['Laptop', 'Mouse', 'Monitor', 'Keyboard'],
        'unit_price': [1200, 25, 300, 75],
        'quantity': [5, 50, 10, 20]
    })

    # TRICK: The Assign Method
    # This allows us to define new columns within a single chain of logic
    df_enhanced = (df
        .assign(
            total_revenue = lambda x: x['unit_price'] * x['quantity'],
            is_high_value = lambda x: x['unit_price'] > 500,
            tax_amount    = lambda x: x['unit_price'] * 0.18
        )
    )

    print(df_enhanced)

if __name__ == "__main__":
    main()
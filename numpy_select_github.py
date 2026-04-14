import pandas as pd
import numpy as np

class RiskAssessment:
    """
    A class to automate categorical labeling based on 
    multiple numerical conditions using vectorized logic.
    """
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def __str__(self):
        return f"Assessment ready for {len(self.df)} records."

    def categorize_credit_risk(self):
        """
        TRICK: np.select()
        This replaces nested 'if' statements or multiple .loc calls.
        It maps conditions to choices in a clean, readable way.
        """
        # 1. Define the conditions
        conditions = [
            (self.df['Credit_Score'] >= 800),
            (self.df['Credit_Score'] >= 700) & (self.df['Credit_Score'] < 800),
            (self.df['Credit_Score'] >= 600) & (self.df['Credit_Score'] < 700)
        ]

        # 2. Define the corresponding labels
        choices = ['Excellent', 'Good', 'Fair']

        # 3. Apply logic (with a 'default' value for anything that doesn't match)
        self.df['Risk_Category'] = np.select(conditions, choices, default='Poor')
        
        return self.df

def main():
    # Sample Dataset: Customer credit scores
    data = {
        'Customer_Name': ['Anna', 'Ben', 'Chloe', 'Dan', 'Eve'],
        'Credit_Score': [850, 720, 650, 580, 790]
    }

    # Initialize the assessment engine
    engine = RiskAssessment(data=data)

    # Execute the labeling logic
    results = engine.categorize_credit_risk()

    # Display Results
    print("--- Credit Risk Evaluation ---")
    print(results)

if __name__ == "__main__":
    main()
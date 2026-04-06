import pandas as pd

class CustomerSegmentation:
    """
    A class to segment customers based on their spending patterns 
    using automated binning techniques.
    """
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def __str__(self):
        return self.df.to_string()

    def segment_by_spending(self):
        """
        Groups customers into 'Budget', 'Mid-Range', and 'Premium' 
        based on their total purchase amount.
        """
        # Define the boundaries for our bins
        bins = [0, 100, 500, float('inf')]
        # Define the labels for each segment
        labels = ['Budget', 'Mid-Range', 'Premium']

        # TRICK: pd.cut creates the categories automatically
        self.df['Segment'] = pd.cut(self.df['Total_Spend'], bins=bins, labels=labels)
        return self.df

    def get_segment_counts(self):
        """Returns how many customers fall into each category."""
        if 'Segment' not in self.df.columns:
            self.segment_by_spending()
        return self.df['Segment'].value_counts()

def main():
    # Sample Dataset: Customer spending data
    raw_data = {
        'Customer_ID': [101, 102, 103, 104, 105, 106],
        'Total_Spend': [45, 120, 650, 35, 480, 900]
    }

    # Initialize the segmentation engine
    engine = CustomerSegmentation(data=raw_data)

    # 1. Perform segmentation
    processed_data = engine.segment_by_spending()

    # 2. Get distribution of segments
    distribution = engine.get_segment_counts()

    # Display Results
    print("--- Processed Customer Data ---")
    print(processed_data)
    
    print("\n--- Market Segment Distribution ---")
    print(distribution)

if __name__ == "__main__":
    main()
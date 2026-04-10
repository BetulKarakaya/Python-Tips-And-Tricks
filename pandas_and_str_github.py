import pandas as pd

class TextDataProcessor:
    """
    A class to demonstrate high-performance string manipulation 
    using Pandas vectorized string accessors.
    """
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def __str__(self):
        return f"Current Text Data:\n{self.df.to_string()}"

    def clean_and_extract(self):
        """
        Cleans the 'Raw_Code' column and extracts 
        specific patterns using vectorized methods.
        """
        # TRICK: Using .str allows us to chain text operations without loops
        processed_df = self.df.assign(
            # 1. Strip whitespace and uppercase
            Clean_Code = self.df['Raw_Code'].str.strip().str.upper(),
            # 2. Extract only the numeric part using Regex
            Serial_Number = self.df['Raw_Code'].str.extract(r'(\d+)'),
            # 3. Check if the code starts with a specific prefix
            Is_Alpha = self.df['Raw_Code'].str.startswith('A')
        )
        return processed_df

def main():
    # Sample Dataset: Irregular product codes
    data = {
        'Raw_Code': ['  a102  ', 'b505', 'A999 ', ' c202', 'A111']
    }

    # Initialize the processor
    processor = TextDataProcessor(data=data)

    # 1. Execute vectorized cleaning
    final_df = processor.clean_and_extract()

    # Display Results
    print("--- Before and After Processing ---")
    print(final_df)

if __name__ == "__main__":
    main()
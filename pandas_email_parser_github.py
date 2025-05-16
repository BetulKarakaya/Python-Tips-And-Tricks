import pandas as pd

class MessyTextParser:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Please provide a valid pandas DataFrame.")
        self.df = df

    @staticmethod
    def extract_email(df, column):
        # Capture email transaction and transfer it to new column
        df["Extracted_Email"] = df[column].str.extract(r"([\w\.-]+@[\w\.-]+\.\w+)")
        return df

def main():
    data = {
        "Notes": [
            "Contact me at betul@example.com for details.",
            "No email here!",
            "Reach us via info@company.org or call.",
            "Send your CV to hr@awesome.dev now!",
            "Hey this is just a @ sign.",
            "One more@."
        ]
    }

    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)

    parser = MessyTextParser(df)
    updated_df = parser.extract_email(df, "Notes")

    print("\nExtracted Emails:\n", updated_df)

if __name__ == "__main__":
    main()

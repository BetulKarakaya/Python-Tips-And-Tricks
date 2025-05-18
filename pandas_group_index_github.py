import pandas as pd

class GroupIndexer:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        self.df = df.copy()
    
    def add_group_index(self, group_cols, index_col_name="GroupIndex"):
        self.df[index_col_name] = (
            self.df.groupby(group_cols).cumcount() + 1
        )
        return self.df

def main():
    data = {
        "Department": ["IT", "IT", "HR", "HR", "IT", "HR"],
        "Name": ["Betül", "Ahmet", "Zeynep", "Ali", "Mert", "Ayşe"]
    }
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)

    indexer = GroupIndexer(df)
    indexed_df = indexer.add_group_index(group_cols=["Department"])
    
    print("\nDataFrame with Group-Based Index:\n", indexed_df)

if __name__ == "__main__":
    main()

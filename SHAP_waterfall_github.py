from sklearn.model_selection import train_test_split
import pandas as pd
import shap
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt


class ModelExplainer:
    def __init__(self, df, target_column):
        self.df = df
        self.X = self.df.drop(target_column, axis=1)
        self.y = self.df[target_column]

    def to_numeric(self):
        object_columns = list(self.X.select_dtypes(include=["object"]).columns)
        self.X = pd.get_dummies(self.X, columns=object_columns, drop_first=True)  

    def split_data(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42)

    def train_model(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)
        print("Model training completed.")

    def explain_model(self):
        self.explainer = shap.TreeExplainer(self.model)
        self.shap_values = self.explainer.shap_values(self.X_test)
        print("SHAP values computed.")

    def plot_summary(self):
        shap.initjs()
        shap.summary_plot(self.shap_values, self.X_test)


    def run(self):
        self.to_numeric()
        self.split_data()
        self.train_model()
        self.explain_model()
        self.plot_summary()


def main():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
    columns = ["Sex", "Length", "Diameter", "Height", "WholeWeight",
               "ShuckedWeight", "VisceraWeight", "ShellWeight", "Rings"]
    abalone_data = pd.read_csv(url, header=None, names=columns)
    explainer = ModelExplainer(abalone_data, "Rings")
    explainer.run()


if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

class ModelExplainer:
    def __init__(self):
        self.X, self.y = make_classification(n_samples=300, n_features=10, n_informative=5, random_state=42)
        self.feature_names = [f'Feature_{i}' for i in range(self.X.shape[1])]
        self.X_df = pd.DataFrame(self.X, columns=self.feature_names)

    def train_model(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(self.X_df, self.y)
        print("Model training completed.")

    def explain_model(self):
        self.explainer = shap.TreeExplainer(self.model)
        self.shap_values = self.explainer.shap_values(self.X_df)
        if isinstance(self.shap_values, list):
            self.shap_values_for_plot = self.shap_values[1] 
        else:
            self.shap_values_for_plot = self.shap_values

        print("SHAP values generated.")

    def plot_summary(self):
        plt.close('all')
        shap.summary_plot(self.shap_values_for_plot, self.X_df, plot_type="bar", show=True)
        print("SHAP summary plot displayed.")

    def run(self):
        self.train_model()
        self.explain_model()
        self.plot_summary()

def main():
    explainer = ModelExplainer()
    explainer.run()

if __name__ == "__main__":
    main()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

class InsightEngine:
    """
    A class to extract 'The Truth' from any trained model 
    by measuring feature sensitivity.
    """
    def __init__(self, model):
        self.model = model

    def rank_features(self, X_test, y_test, feature_names):
        
        result = permutation_importance(
            self.model, X_test, y_test, n_repeats=10, random_state=42, n_jobs=-1
        )
        
        sorted_idx = result.importances_mean.argsort()
        labels_to_plot = np.array(feature_names)[sorted_idx].tolist()
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.boxplot(result.importances[sorted_idx].T, vert=False, labels=labels_to_plot)
        
        ax.set_title("Permutation Importances (Test Set)")
        fig.tight_layout()
        plt.show()

def main():
  
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    engine = InsightEngine(clf)
    engine.rank_features(X_test, y_test, data.feature_names)

if __name__ == "__main__":
    main()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import RepeatedStratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, roc_auc_score

class Validation:
    def __init__(self):
        self.X, self.y = make_classification(n_samples=500, n_features=20, n_informative=10, n_redundant=5,
                                             n_clusters_per_class=2, random_state=42)

    def classify_and_validate(self):
        # Define classifier
        self.clf = RandomForestClassifier(n_estimators=100, random_state=42)

        # Define evaluation method: repeated stratified k-fold CV
        self.cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=10, random_state=42)

        # Use ROC AUC as evaluation metric
        self.roc_auc = make_scorer(roc_auc_score, needs_proba=True)

        # Perform cross-validation
        self.scores = cross_val_score(self.clf, self.X, self.y, scoring=self.roc_auc, cv=self.cv, n_jobs=-1)

    def display_scores(self):
        mean_score = np.mean(self.scores)
        std_score = np.std(self.scores)

        print(f"- Mean ROC AUC: {mean_score:.4f}")
        print(f"- Std Deviation: {std_score:.4f}")

        # Comment based on mean score
        if mean_score >= 0.90:
            print("Excellent model! Very high ROC AUC indicates strong separability.")
        elif mean_score >= 0.80:
            print("Good model. ROC AUC is decent, but there might still be room for improvement.")
        elif mean_score >= 0.70:
            print("Moderate performance. Consider feature engineering, hyperparameter tuning, or trying other models.")
        else:
            print("Low performance. Model is not separating classes well. Needs serious improvement!")

        # Comment based on std deviation
        if std_score < 0.01:
            print("Very stable results across folds (low variance).")
        elif std_score < 0.03:
            print("Results are relatively consistent, but there is slight variance.")
        else:
            print("High variance! Model is unstable across folds. Try stratification, balancing, or more robust models.")


    def visualize_distribution(self):
        plt.figure(figsize=(10, 5))
        sns.histplot(self.scores, kde=True, color="#b1a9f7", bins=20)
        plt.title("Distribution of ROC AUC Scores", fontsize=14)
        plt.xlabel("ROC AUC Score")
        plt.ylabel("Frequency")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()


def main():
    validator = Validation()
    validator.classify_and_validate()
    validator.display_scores()
    validator.visualize_distribution()

if __name__ == "__main__":
    main()

import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

class ModelValidator:
    """
    A class to perform rigorous cross-validation on 
    ML pipelines to ensure statistical stability.
    """
    def __init__(self, cv_folds=5):
        self.cv_folds = cv_folds
        # Using Ridge Regression (Linear + L2 Regularization)
        self.model_pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('regressor', Ridge())
        ])

    def validate(self, X, y):
        """
        TRICK: cross_val_score()
        It automates the splitting, fitting, and scoring process 
        multiple times to prevent overfitting.
        """
        scores = cross_val_score(
            self.model_pipeline, 
            X, y, 
            cv=self.cv_folds, 
            scoring='r2' # R-squared metric
        )
        return scores

def main():
    # Generate 1000 samples of synthetic regression data
    X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)

    # Initialize Validator
    validator = ModelValidator(cv_folds=5)
    
    # Execute K-Fold Validation
    performance_scores = validator.validate(X, y)

    # Analyze results
    print("--- 5-Fold Cross-Validation Results ---")
    print(f"Individual Scores: {performance_scores.round(4)}")
    print(f"Mean R² Score:    {np.mean(performance_scores):.4f}")
    print(f"Standard Dev:     {np.std(performance_scores):.4f}")

if __name__ == "__main__":
    main()
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.experimental import enable_halving_search_cv  # Required for HalvingSearch
from sklearn.model_selection import HalvingGridSearchCV, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier

class AutomatedModelOptimizer:
    """
    Implements a Nested Cross-Validation framework to perform 
    unbiased model evaluation and efficient parameter optimization.
    """
    def __init__(self, estimator, param_grid):
        self.estimator = estimator
        self.param_grid = param_grid
        
    def execute_nested_cv(self, X, y):
        """
        TRICK: Nested CV (Inner vs Outer Loop)
        Inner Loop: HalvingGridSearchCV finds the best parameters.
        Outer Loop: cross_val_score evaluates the performance of the 
        entire 'Searching Process'.
        """
        # Define the Inner Loop (Parameter Search)
        # HalvingGridSearchCV is much faster than standard GridSearchCV
        inner_cv = KFold(n_splits=3, shuffle=True, random_state=42)
        parameter_search = HalvingGridSearchCV(
            self.estimator, 
            self.param_grid, 
            cv=inner_cv, 
            factor=3,        # Darwinian: Only the top 1/3 move to next round
            n_jobs=-1,
            resource='n_samples' # Increase data as we narrow down params
        )

        # Define the Outer Loop (Model Evaluation)
        outer_cv = KFold(n_splits=5, shuffle=True, random_state=42)
        
        # This executes the entire search within each fold of the outer CV
        nested_scores = cross_val_score(
            parameter_search, X, y, cv=outer_cv, scoring='accuracy'
        )
        
        return nested_scores

def main():
   
    data = load_breast_cancer()
    X, y = data.data, data.target

    # Using Gradient Boosting (SOTA for tabular data)
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('gb', GradientBoostingClassifier(random_state=42))
    ])

    param_grid = {
        'gb__n_estimators': [50, 100, 200],
        'gb__learning_rate': [0.01, 0.1, 0.2],
        'gb__max_depth': [3, 5, 7]
    }

    optimizer = AutomatedModelOptimizer(pipeline, param_grid)
    print("Executing Nested Cross-Validation (This may take a moment)...")
    
    scores = optimizer.execute_nested_cv(X, y)

    print("\n" + "="*30)
    print("ADVANCED MODEL REPORT")
    print("="*30)
    print(f"Nested CV Accuracy Scores: {scores}")
    print(f"Mean Performance:         {np.mean(scores):.4f}")
    print(f"Performance Variance:     {np.std(scores):.4f}")
    print("="*30)

if __name__ == "__main__":
    main()
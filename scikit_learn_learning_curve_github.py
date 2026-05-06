import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
from sklearn.datasets import load_digits

class ModelDiagnostician:
    """
    A class to diagnose whether a model requires more training data 
    or increased complexity using Learning Curves.
    """
    def __init__(self, model):
        self.model = model

    def plot_learning_curve(self, X, y):
        """
        TRICK: learning_curve()
        Trains the model on increasingly larger subsets of the data 
        (from 10% to 100%) to observe how performance scales.
        """
        # Calculate scores for 5 different training set sizes
        train_sizes, train_scores, test_scores = learning_curve(
            self.model, X, y, cv=5, n_jobs=-1, 
            train_sizes=np.linspace(0.1, 1.0, 5),
            scoring='accuracy'
        )

        # Calculate Mean and Standard Deviation for shading
        train_mean = np.mean(train_scores, axis=1)
        train_std = np.std(train_scores, axis=1)
        test_mean = np.mean(test_scores, axis=1)
        test_std = np.std(test_scores, axis=1)

        # Visualization
        plt.figure(figsize=(10, 6))
        
        # Plot Training Scores
        plt.plot(train_sizes, train_mean, 'o-', color="r", label="Training Score")
        plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.1, color="r")
        
        # Plot Cross-Validation Scores
        plt.plot(train_sizes, test_mean, 'o-', color="g", label="Cross-Validation Score")
        plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.1, color="g")

        # Aesthetics
        plt.title("Learning Curves (Scaling Analysis)")
        plt.xlabel("Number of Training Examples")
        plt.ylabel("Accuracy Score")
        plt.legend(loc="best")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

def main():
    # Load a complex dataset (Handwritten Digits)
    digits = load_digits()
    X, y = digits.data, digits.target

    # Select a Model (Support Vector Machine)
    # Using a low gamma to observe the learning transition
    model = SVC(gamma=0.001)

    diagnostician = ModelDiagnostician(model)
    diagnostician.plot_learning_curve(X, y)

if __name__ == "__main__":
    main()
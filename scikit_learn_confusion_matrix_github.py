import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay

class ErrorVisualizer:
    """
    A class to visualize classification performance and 
    identify specific misclassification patterns.
    """
    def __init__(self, model):
        self.model = model

    def plot_errors(self, X_test, y_test, class_names):
        """
        TRICK: ConfusionMatrixDisplay.from_estimator()
        It automatically handles predictions on X_test, calculates the 
        matrix against y_test, and generates a heatmap in one line.
        """
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Visualize the matrix in seconds
        display = ConfusionMatrixDisplay.from_estimator(
            self.model, 
            X_test, 
            y_test, 
            display_labels=class_names,
            cmap=plt.cm.Blues, # Color palette
            ax=ax
        )
        
        ax.set_title("Model Confusion Matrix: Mapping the Mistakes")
        plt.show()
        return display

def main():
    # Load the classic breast cancer diagnostic dataset (Malignant/Benign)
    data = load_breast_cancer()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # Train a quick model
    clf = RandomForestClassifier(n_estimators=10, random_state=42)
    clf.fit(X_train, y_train)


    visualizer = ErrorVisualizer(clf)
    visualizer.plot_errors(X_test, y_test, data.target_names)

if __name__ == "__main__":
    main()
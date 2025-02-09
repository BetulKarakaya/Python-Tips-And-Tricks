import numpy as np
import matplotlib.pyplot as plt

class MultipleLinearRegression:

    def __init__(self, X, Y):
        """
        Initialize the Multiple Linear Regression model.
        
        Parameters:
        X (ndarray): Feature matrix (independent variables).
        Y (ndarray): Target variable (dependent variable).
        """
        self.X = np.array(X, dtype=float)  # Convert input to NumPy array
        self.Y = np.array(Y, dtype=float)  # Convert target variable to NumPy array
        
        # Add a column of ones for the intercept (bias term)
        # -------------------------------------------------
        # In multiple linear regression, the model is: 
        #     Y = b0 + b1*X1 + b2*X2 + ... + bn*Xn
        # Here, "b0" is the intercept (bias), which does not multiply any X values.
        # To include this in matrix operations, we add a column of ones to X.
        ones = np.ones((self.X.shape[0], 1))  # Create a column of ones (same row count as X)
        self.X = np.hstack((ones, self.X))   # Concatenate ones with the original feature matrix

        # Compute the coefficients using the Normal Equation
        # --------------------------------------------------
        # The Normal Equation formula for multiple linear regression is:
        #     m = (X^T * X)^(-1) * X^T * Y
        # where:
        #     X   → Feature matrix (including bias term)
        #     Y   → Target variable
        #     X^T → Transpose of X
        #     (X^T * X)^(-1) → Inverse of X^T * X
        # This formula finds the optimal values for the regression coefficients (m).
        self.m = np.linalg.inv(self.X.T @ self.X) @ self.X.T @ self.Y  # Compute m using matrix operations


    def calculate_y_pred(self):
        """ Compute predicted Y values using the regression coefficients. """
        self.Y_pred = self.X @ self.m  # Matrix multiplication

    def visualize(self):
        """ 
        Visualize the regression for the first two features 
        (only works when there are two independent variables).
        """
        if self.X.shape[1] != 3:  # Bias + 2 features
            print("Visualization is only supported for 2D regression.")
            return

        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(self.X[:, 1], self.X[:, 2], self.Y, color="#fc4444", label="Real Data")
        ax.scatter(self.X[:, 1], self.X[:, 2], self.Y_pred, color="#3505ad", label="Predicted Data")

        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")
        
        ax.set_title("Multiple Linear Regression (Least Squares Method)")
        ax.legend()
        plt.show()


def main():
    np.random.seed(42)  # Set random seed for reproducibility

    # Generate random feature values
    X1 = np.random.randint(1, 100, 30)  # Feature 1
    X2 = np.random.randint(1, 100, 30)  # Feature 2

    # Create a target variable with some noise
    Y = 3 * X1 + 2 * X2 + 8 + np.random.randn(30) * 50  # Y = 3X1 + 2X2 + 8 + noise

    # Stack features together
    X = np.column_stack((X1, X2))

    model = MultipleLinearRegression(X, Y)
    model.calculate_y_pred()
    model.visualize()


if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt


""" 
y_pred = mX+b
m= ( ∑(X−X mean) ⋅(Y−Y mean)) / (∑(X−X mean) * ∑(X−X mean))
​b=Ymean−m⋅X mean
"""



class LinearRegression:

    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
        self.X_mean = np.mean(self.X)
        self.Y_mean = np.mean(self.Y)
        self.m =  np.sum((self.X - self.X_mean) * (self.Y - self.Y_mean)) / np.sum((self.X - self.X_mean) ** 2)
        self.b = self.Y_mean - (self.m * self.X_mean)

    def calculate_y_pred(self):
        self.Y_pred = (self.m * self.X) + self.b

    def visualize(self):
        plt.figure(figsize= (12,5))
        plt.scatter(self.X, self.Y, color = "#1f0075", label = "Real Data")
        plt.plot(self.X, self.Y_pred, color = "#ffc445", label = "Y Prediction")
        
        plt.title("Linear Regression With Least Squares Method", color = "#29251b", fontsize = 15)
        plt.yticks(np.arange(0,max(self.Y)+1,10))
        plt.grid(True)
        plt.gca().set_axisbelow(True)
        plt.legend()
        plt.show()
def main():
    np.random.seed(42)
    X = np.arange(0,51,2)
    
    Y = 3 * X + (5 +  np.random.randn(26) * 5) # The Real Relationship Between X and Y

    app = LinearRegression(X, Y)
    app.calculate_y_pred()
    app.visualize()

if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt

class BinomialSimulation:
    def __init__(self, n, p, num_samples):
    
        self.n = n
        self.p = p
        self.num_samples = num_samples
        self.samples = None

    def run_simulation(self):
        
        self.samples = np.random.binomial(self.n, self.p, self.num_samples)
        
    def calculate_statistics(self):
        
        if self.samples is None:
            raise ValueError("Simulation has not been run!")
        
        mean = np.mean(self.samples)
        std_dev = np.std(self.samples)
        return mean, std_dev

    def count_successes(self, threshold):
        
        if self.samples is None:
            raise ValueError("Simulation has not been run!")
        
        return np.sum(self.samples >= threshold)

    def visualize_distribution(self):
    
        if self.samples is None:
            raise ValueError("Simulation has not been run!")
        
        plt.figure(figsize=(10,6))
        plt.hist(self.samples, bins=30, color = "#7457b3", edgecolor="black", alpha=0.7)
        plt.title(f"Binomial Distribution (n={self.n}, p={self.p}) - {self.num_samples} Samples", fontsize=14)
        plt.xlabel("Number of Successes", fontsize=12)
        plt.ylabel("Frequency", fontsize=12)
        plt.show()

    def run(self):
        self.run_simulation()
        mean, std_dev = self.calculate_statistics()
        success_count = self.count_successes(10)

        print(f"Mean: {mean:.2f}, Standard Deviation: {std_dev:.2f}")
        print(f"Number of samples with 10 or more successes: {success_count}")
        self.visualize_distribution()

def main():
    
    n = 20  
    p = 0.5  
    num_samples = 10000  

    simulation = BinomialSimulation(n, p, num_samples)
    simulation.run()

if __name__ == "__main__":
    main()

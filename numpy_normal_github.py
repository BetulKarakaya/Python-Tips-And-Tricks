import pandas as pd
import numpy as np

class MonteCarloSimulator:
    """
    A class to perform probabilistic simulations using 
    vectorized random sampling from normal distributions.
    """
    def __init__(self, iterations=10000):
        self.iterations = iterations

    def __str__(self):
        return f"Simulator configured for {self.iterations} iterations."

    def simulate_profit(self, revenue_mean, revenue_std, cost_mean, cost_std):
        """
        TRICK: Vectorized Random Sampling.
        Instead of a loop, we generate 10,000 samples for revenue 
        and 10,000 for costs simultaneously.
        """
        # Generate random scenarios for Revenue and Costs
        rev_samples = np.random.normal(revenue_mean, revenue_std, self.iterations)
        cost_samples = np.random.normal(cost_mean, cost_std, self.iterations)

        # Calculate profit for every single universe
        profit_samples = rev_samples - cost_samples

        # Create a summary of results
        results = {
            'Expected Profit': np.mean(profit_samples),
            'Max Potential Profit': np.max(profit_samples),
            'Risk of Loss (%)': (np.sum(profit_samples < 0) / self.iterations) * 100,
            '95% Confidence Interval': np.percentile(profit_samples, [2.5, 97.5])
        }
        return results

def main():
    # Initialize the simulator
    simulator = MonteCarloSimulator(iterations=100000)
    print(simulator)

    # Scenario: Launching a new product
    # Revenue is expected to be $500k but could vary by $100k
    # Costs are expected to be $350k but could vary by $50k
    simulation_results = simulator.simulate_profit(
        revenue_mean=500000, revenue_std=100000, 
        cost_mean=350000, cost_std=50000
    )

    # Display Results
    print("\n--- Monte Carlo Financial Forecast ---")
    for key, value in simulation_results.items():
        if isinstance(value, np.ndarray):
            print(f"{key}: ${value[0]:,.2f} to ${value[1]:,.2f}")
        elif 'Risk' in key:
            print(f"{key}: {value:.2f}%")
        else:
            print(f"{key}: ${value:,.2f}")

if __name__ == "__main__":
    main()
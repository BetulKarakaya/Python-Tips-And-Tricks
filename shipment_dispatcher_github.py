from functools import cmp_to_key, lru_cache, partial, wraps
import time

def monitor_performance(func):
    """Decorator to track execution time and metadata."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[METRIC] '{func.__name__}' executed in {end_time - start_time:.6f}s")
        return result
    return wrapper

class ShipmentDispatcher:
    def __init__(self, packages):
        self.packages = packages

    @lru_cache(maxsize=256)
    def calculate_delivery_cost(self, weight, distance, fuel_surcharge):
        """
        Simulates a heavy computational task or an API call 
        to calculate shipping costs based on dynamic variables.
        """
        time.sleep(0.05)  # Artificial latency
        return (weight * 0.5) + (distance * 0.2) + fuel_surcharge

    def compare_shipments(self, p1, p2, fuel_surcharge=1.5):
        """
        Priority Logic:
        1. 'Express' shipping always comes before 'Standard'.
        2. If same type, the one with higher delivery cost (higher revenue) comes first.
        """
        # 1. Check Priority Type
        if p1["type"] == "Express" and p2["type"] == "Standard":
            return -1
        if p1["type"] == "Standard" and p2["type"] == "Express":
            return 1

        # 2. Check Calculated Cost (Revenue Priority)
        cost1 = self.calculate_delivery_cost(p1["weight"], p1["distance"], fuel_surcharge)
        cost2 = self.calculate_delivery_cost(p2["weight"], p2["distance"], fuel_surcharge)

        if cost1 > cost2: return -1
        if cost1 < cost2: return 1
        
        return 0

    @monitor_performance
    def get_priority_queue(self, current_fuel_rate=2.0):
        """
        Uses partial to fix the fuel rate and cmp_to_key to 
        transform the comparison logic into a sort key.
        """
        # Pre-configure the comparison function with the current fuel rate
        optimized_compare = partial(self.compare_shipments, fuel_surcharge=current_fuel_rate)
        
        # Sort using the converted key
        return sorted(self.packages, key=cmp_to_key(optimized_compare))

def main():
    # Dataset with some duplicate values to demonstrate lru_cache efficiency
    shipments = [
        {"id": "A101", "type": "Standard", "weight": 10, "distance": 100},
        {"id": "B202", "type": "Express", "weight": 5, "distance": 50},
        {"id": "C303", "type": "Express", "weight": 20, "distance": 200},
        {"id": "D404", "type": "Standard", "weight": 10, "distance": 100}, # Same as A101
    ]

    dispatcher = ShipmentDispatcher(shipments)

    print("--- First Pass (Cache is Cold) ---")
    priority_list_1 = dispatcher.get_priority_queue(current_fuel_rate=2.5)

    print("\n--- Second Pass (Cache is Hot - Instant Execution) ---")
    priority_list_2 = dispatcher.get_priority_queue(current_fuel_rate=2.5)

    print("\nFinal Priority Queue:")
    for item in priority_list_2:
        print(f"ID: {item['id']} | Type: {item['type']} | Dist: {item['distance']}km")

if __name__ == "__main__":
    main()
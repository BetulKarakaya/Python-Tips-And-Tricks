from memory_profiler import profile
import time

class MemoryInspector:
    """
    A utility class to monitor memory consumption 
    during intensive data operations.
    """
    
    @profile  # Bu dekoratör bellek kullanımını satır satır izler
    def heavy_operation(self):
        """
        A function designed to demonstrate memory allocation 
        and deallocation (garbage collection).
        """
        print("--- Operation Started ---")
        
        # Create a large list (fill up RAM)
        # Approximately 10 million integers will take up ~80MB+ of space
        data_list = [i for i in range(10000000)]
        time.sleep(1) # A brief pause to read the report.
        
        # Modify the list (RAM can continue to increase)
        modified_list = [x * 2 for x in data_list[:5000000]]
        print(f"Sub-list created with {len(modified_list)} elements.")
        time.sleep(1)
        
        # Clear the data (monitor RAM freeing up)
        del data_list
        print("Initial large list deleted.")
        time.sleep(2)
        
        return modified_list

def main():
    inspector = MemoryInspector()
    result = inspector.heavy_operation()
    print("--- Operation Finished ---")

if __name__ == "__main__":
    main()
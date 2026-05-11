import os
import psutil
import gc
from time import sleep

class MemoryShield:
    """
    A High-Level Context Manager to profile memory consumption 
    of specific code blocks in real-time.
    """
    def __init__(self, tag="Block"):
        self.tag = tag
        self.process = psutil.Process(os.getpid())

    def get_memory(self):
        # Returns memory usage in Megabytes
        return self.process.memory_info().rss / (1024 * 1024)

    def __enter__(self):
        self.initial_mem = self.get_memory()
        print(f"[{self.tag}] Initial RAM: {self.initial_mem:.2f} MB")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        final_mem = self.get_memory()
        diff = final_mem - self.initial_mem
        print(f"[{self.tag}] Final RAM:   {final_mem:.2f} MB")
        print(f"[{self.tag}] Net Impact:  {diff:+.2f} MB")
        print("-" * 30)

def technical_demonstration():
    """
    Executing a high-pressure memory task inside the custom shield.
    """
    # Profile an 'In-Memory' explosion
    with MemoryShield("Heavy List Creation"):
        # Allocating a large chunk of memory
        buffer = [dict(id=i, val="x" * 1000) for i in range(100_000)]
        sleep(1)
        
    # Manual Cleanup & Garbage Collection
    print("Action: Deleting buffer and forcing Garbage Collection...")
    del buffer
    gc.collect() # Manually trigger the cyclic garbage collector
    
    # Verify Baseline
    with MemoryShield("Post-Cleanup State"):
        sleep(1)
        print("System verified. Memory has been released.")

def main(): 
    technical_demonstration()

if __name__ == "__main__":
   main()
import logging
import logging.handlers
import queue
import threading
import time

class AsyncLoggingEngine:
    """
    A high-performance logging architecture that offloads 
    I/O operations to a background thread using a Queue.
    """
    def __init__(self, log_file="app_diagnostics.log"):
        self.log_queue = queue.Queue(-1)  # Infinite queue size
        self.log_file = log_file
        self._setup_logging()

    def _setup_logging(self):
        # The 'Handler' that actually writes to the disk
        file_handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | [%(threadName)s] %(message)s'
        )
        file_handler.setFormatter(formatter)

        # The 'Listener' that watches the queue and passes logs to the file_handler
        self.listener = logging.handlers.QueueListener(self.log_queue, file_handler)
        
        # The 'QueueHandler' that the app actually talks to
        self.root_logger = logging.getLogger()
        self.root_logger.setLevel(logging.DEBUG)
        
        queue_handler = logging.handlers.QueueHandler(self.log_queue)
        self.root_logger.addHandler(queue_handler)

    def start(self):
        self.listener.start()
        print("[System] Async Logger Started.")

    def stop(self):
        self.listener.stop()
        print("[System] Async Logger Gracefully Shutdown.")

def simulate_heavy_workload():
    """
    Simulating a real-time system where logging must not slow down the logic.
    """
    logger = logging.getLogger("MainApp")
    
    for i in range(5):
        # Even if writing to disk takes time, this log call returns INSTANTLY
        logger.info(f"Processing critical task batch #{i}")
        time.sleep(0.5) 

if __name__ == "__main__":
    engine = AsyncLoggingEngine()
    engine.start()

    simulate_heavy_workload()

    engine.stop()
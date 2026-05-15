import logging
import os

class DiagnosticSystem:
    """
    A foundational system class showcasing standard logging configuration 
    with dual-routing (Console and File).
    """
    def __init__(self, log_filename="system_logs.log"):
        self.log_filename = log_filename
        self._initialize_logger()

    def _initialize_logger(self):
        # Create a dedicated logger instance
        self.logger = logging.getLogger("CoreApplication")
        self.logger.setLevel(logging.DEBUG)  # Capture everything at the root level

        # Prevent duplicate logs if initialized multiple times
        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        # Create a File Handler (Captures detailed Debug logs)
        file_handler = logging.FileHandler(self.log_filename)
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | [%(filename)s:%(lineno)d] | %(message)s'
        )
        file_handler.setFormatter(file_formatter)

        # Create a Console Handler (Captures clean Info/Warning logs for terminal)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(levelname)s: %(message)s')
        console_handler.setFormatter(console_formatter)

        # Attach handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def process_transaction(self, amount, user_id):
        """
        Simulates a real-world application operation utilizing different log levels.
        """
        self.logger.debug(f"Starting transaction for User ID: {user_id} with Amount: ${amount}")
        
        if amount <= 0:
            self.logger.error(f"Transaction failed: Invalid amount ${amount} for User ID: {user_id}")
            return False
            
        if amount > 10000:
            self.logger.warning(f"High-value transaction flagged for User ID: {user_id} (${amount})")
            
        self.logger.info(f"Transaction successfully processed for User ID: {user_id}")
        return True

def main():
    # Initialize the system
    sys_monitor = DiagnosticSystem()
    
    print("--- Executing Script (Watch the Console Output) ---\n")
    
    # Run some test cases
    sys_monitor.process_transaction(250, "user_01")      # Normal behavior
    sys_monitor.process_transaction(15000, "user_02")    # Triggers a warning
    sys_monitor.process_transaction(-50, "user_03")      # Triggers an error

    print(f"\n--- Script Finished. Check '{sys_monitor.log_filename}' for full DEBUG logs. ---")

if __name__ == "__main__":
    main()
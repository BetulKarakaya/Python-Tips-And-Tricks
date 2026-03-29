from collections import Counter
from functools import cached_property, wraps

def log_event(func):
    """Decorator to announce analysis steps."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[ANALYSIS] Running: {func.__name__.replace('_', ' ').title()}")
        return func(*args, **kwargs)
    return wrapper

class LogAnalyzer:
    def __init__(self, server_logs):
        # server_logs: List of strings like "ERROR", "INFO", "DEBUG"
        self.raw_logs = server_logs

    @cached_property
    def log_counts(self):
        """
        Calculates frequencies once and caches the Counter object.
        Uses functools.cached_property for efficiency.
        """
        return Counter(self.raw_logs)

    @log_event
    def get_severity_report(self, threshold=1):
        """Returns logs that occurred more than 'threshold' times."""
        # most_common() returns a list of (element, count) tuples
        return [item for item, count in self.log_counts.items() if count >= threshold]

    @log_event
    def compare_with_baseline(self, baseline_logs):
        """
        Uses Counter arithmetic to find 'excess' logs 
        compared to a normal baseline.
        """
        baseline_counter = Counter(baseline_logs)
        
        # Counter Arithmetic: Subtracting baseline from current logs
        # This shows only the increase in errors/logs
        diff = self.log_counts - baseline_counter
        return diff

    @log_event
    def get_critical_overlap(self, other_server_logs):
        """
        Finds the common minimum log counts between two servers 
        using the Intersection (&) operator.
        """
        other_counter = Counter(other_server_logs)
        common_issues = self.log_counts & other_counter
        return common_issues

def main():
    # Current server logs
    server_a = ["ERROR", "INFO", "ERROR", "DEBUG", "ERROR", "INFO", "WARNING"]
    
    # Typical baseline for a healthy server
    healthy_baseline = ["ERROR", "INFO", "INFO", "DEBUG"]
    
    # Another server's logs for comparison
    server_b = ["ERROR", "ERROR", "CRITICAL", "WARNING"]

    analyzer = LogAnalyzer(server_a)

    # 1. Most Common (Top 2)
    print(f"Top Logs: {analyzer.log_counts.most_common(2)}")

    # 2. Difference (Anomaly Detection)
    anomalies = analyzer.compare_with_baseline(healthy_baseline)
    print(f"Anomalies (Current - Baseline): {anomalies}")

    # 3. Intersection (Shared Critical Issues)
    shared = analyzer.get_critical_overlap(server_b)
    print(f"Shared Issues across servers: {shared}")

if __name__ == "__main__":
    main()
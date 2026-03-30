from functools import wraps

def log_process(func):
    """Decorator to log which cleaning stage is running."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[PROCESS] Running: {func.__name__.replace('_', ' ').upper()}")
        return func(*args, **kwargs)
    return wrapper

class DataSanitizer:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @log_process
    def apply_filters(self, filters):
        """
        Applies a list of lambda filters to the raw data.
        'filters' is a list of lambda functions.
        """
        # Lambda functions are used here to process each item in one line
        processed_data = self.raw_data
        for f in filters:
            processed_data = [f(item) for item in processed_data]
        return processed_data

def main():
    # Sample dirty data: Extra spaces, mixed casing
    dirty_emails = ["  USER1@gmail.com  ", "admin@PyThon.org", "   INFO@service.io "]

    sanitizer = DataSanitizer(dirty_emails)

    # Defining simple lambda rules:
    # 1. Strip spaces
    # 2. Convert to lowercase
    # 3. Mask domain (just for a professional touch)
    cleaning_rules = [
        lambda x: x.strip(),
        lambda x: x.lower(),
        lambda x: x.replace("@", " [at] ")
    ]

    clean_data = sanitizer.apply_filters(cleaning_rules)

    print("\nSanitized Results:")
    for email in clean_data:
        print(f"-> {email}")

if __name__ == "__main__":
    main()
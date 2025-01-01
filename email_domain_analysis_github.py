from collections import defaultdict

def email_domain_analyzer(emails):
    """
    Analyze email addresses and count occurrences of each domain using defaultdict.
    """

    # Using defaultdict to avoid KeyError:
    # defaultdict automatically initializes a default value for a key if it doesn't exist.
    # For example:
    # If the default factory is int, any new key will start with the value 0.
    # This is particularly useful for counting occurrences or grouping data.

    # defaultdict initializes with 0 for unseen domains
    domain_counts = defaultdict(int)

    for email in emails:
        # Split the email to extract the domain
        domain = email.split("@")[-1]
        domain_counts[domain] += 1

    # Sort domains by frequency
    sorted_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)

    # Print results in a pretty way
    print("📧 Email Domain Analysis 📧")
    print("-" * 30)
    for domain, count in sorted_domains:
        print(f"{domain}: {count} email(s)")

def main():
    
    email_list = [
        "alice@example.com",
        "bob@gmail.com",
        "charlie@example.com",
        "dave@yahoo.com",
        "eve@gmail.com",
        "frank@outlook.com",
        "grace@yahoo.com",
        "hank@example.com",
    ]

    email_domain_analyzer(email_list)
if __name__ == "__main__":
   main()

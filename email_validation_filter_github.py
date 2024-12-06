def validate_emails(email_list):
    
    return list(filter(
    lambda email: (
        email.count("@") == 1 and  # Ensure the email contains exactly one "@" symbol (valid format).
        all(email.split("@")) and  # Split the email at "@" and check that both parts (local and domain) are non-empty.
        len((domain_parts := email.split("@")[1].split("."))) >= 2 and  # Split the domain part at "." and ensure it has at least two parts (e.g., "domain.com").
        all(domain_parts)  # Check that none of the parts in the domain are empty (e.g., "domain..com" is invalid).
    ),
    email_list  # The list of emails to be filtered.
))



if __name__ == "__main__":
    emails = [
        "john.doe@gmail.com",
        "invalid-email",
        "jane.doe@company",
        "alice123@domain.com",
        "bob@.com",
        "john@.gmail",
        "charlie@valid.org"
    ]

    valid_list = validate_emails(emails)

    print("Original Emails:", emails)
    print("Valid Emails:", valid_list)

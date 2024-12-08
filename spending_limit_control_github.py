def spending_limit_control(transaction_list,spending_limit):

    # Filter transactions exceeding the limit using lambda
    # The filter function iterates through each transaction in the dataset
    # For each transaction, the lambda function checks if the amount (txn[1]) exceeds the spending limit
    # If the condition is True, the transaction is included in the result
    return list(filter(lambda txn: txn[1] > spending_limit, transaction_list))

if __name__ == "__main__":

    # Sample dataset of credit card transactions (Transaction ID, Amount in USD)
    transactions = [
        ("TXN001", 45.50),
        ("TXN002", 120.75),
        ("TXN003", 320.00),
        ("TXN004", 15.00),
        ("TXN005", 85.30),
        ("TXN006", 450.00),
        ("TXN007", 25.40),
    ]

    # Set a spending limit
    spending_limit = 100.00

    # Filter transactions exceeding the limit using lambda
    high_spending_transactions = spending_limit_control(transactions, spending_limit)

    # Display results
    print("High Spending Transactions:")
    for txn_id, amount in high_spending_transactions:
        print(f"Transaction ID: {txn_id}, Amount: ${amount:.2f}")

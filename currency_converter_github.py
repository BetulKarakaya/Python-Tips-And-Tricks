def safe_currency_converter(amount, from_currency, to_currency, exchange_rates):
    """
    Converts a given amount from one currency to another using exchange rates.
    Handles potential exceptions like missing rates or invalid inputs.
    """
    try:
        # Check if currencies exist in the exchange rates
        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            raise KeyError(f"Exchange rate for {from_currency} or {to_currency} is missing!")
        
        # Simulate a potential runtime issue: Negative or zero amounts
        if amount <= 0:
            raise ValueError("Amount must be greater than zero!")
        
        # Convert the amount
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * rate

        return round(converted_amount, 2)
    
    except KeyError as ke:
        print(f"Error: {ke}")
        print("Tip: Ensure all required exchange rates are included in the database.")
    except ValueError as ve:
        print(f"Error: {ve}")
        print("Tip: Enter a positive amount for conversion.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        print("Please contact support or try again.")
    finally:
        print("\n--- Conversion Attempt Completed ---\n")

def display_currency(exchange_rates):
    for key in exchange_rates:
        print(f'{key}', end= " ")
    
    print("\n-----------------------------------\n\n")
def main():
   
   # Base currency ----> 1 USD = 0.85 EUR 
    exchange_rates = {
        "USD": 1.0,    
        "EUR": 0.85,
        "JPY": 110.0,
        "GBP": 0.75,
        "TRY": 35
    }

    try:
        print("Welcome to the Currency Converter!\n\n---Suportted Currency Table---")
        display_currency(exchange_rates = exchange_rates)
        
        #inputs
        amount = float(input("Enter the amount you want to convert: "))
        from_currency = input("Enter the source currency (e.g., USD, EUR): ").strip().upper()
        to_currency = input("Enter the target currency (e.g., USD, EUR): ").strip().upper()
        
        result = safe_currency_converter(amount, from_currency, to_currency, exchange_rates)
        
        if result is not None:
            print(f"\nConverted Amount: {amount} {from_currency} = {result} {to_currency}")
    
    except ValueError:
        print("Invalid input. Please enter a valid numerical amount.")


if __name__ == "__main__":
    main()
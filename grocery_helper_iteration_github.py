 # Iteration Example: Grocery Shopping List

def calculate_cost(groceries,prices):
    
    total_cost = 0
    for item in grocery_list:
        total_cost += prices[item]
    return total_cost

def cost_more_than(groceries,limit, equal = False):
    if(equal):
        expensive_items = [item for item in groceries if prices[item] >= limit]
    else:
        expensive_items = [item for item in groceries if prices[item] > limit]
    return expensive_items

def cost_less_than(groceries, limit, equal = False):
    if(equal):
        cheap_items = [item for item in groceries if prices[item] >= limit]
    else:
        cheap_items = [item for item in groceries if prices[item] > limit]
    return cheap_items

def display_with_price(groceries, prices):
    print(f"\n---MY GROCERY LIST---")
    for i, item in enumerate(groceries):  # Using enumerate for index tracking
        print(f"{i}. Purchased {item} for ${prices[item]:.2f}")

def display_price_list(prices):
    print("f\n---PRICE OF GROCERY ITEMS---")
    for key, price in prices.items():  
        print(f"{key} -> Price: ${price}")

if __name__ == "__main__":

    # A list representing items to buy from the grocery store
    grocery_list = ["apples", "bananas", "bread", "milk", "eggs"]

    # A dictionary representing prices for each grocery item
    prices = {"apples": 1.2, "bananas": 0.5, "bread": 2.0, "milk": 1.5, "eggs": 3.0}

    
    display_price_list(prices)   
    display_with_price(grocery_list, prices)
    
    total_cost = calculate_cost(grocery_list, prices)
    print(f"\n---TOTAL COST OF MY GROCERY LIST---")
    print(f"The total cost of your grocery list is: ${total_cost:.2f}")
    
    limit = 1.5
    print(f"\n---ITEMS WORTH ${limit} AND ABOVE---")
    expensive_items = cost_more_than(grocery_list, limit, equal= True)
    print(expensive_items)
    

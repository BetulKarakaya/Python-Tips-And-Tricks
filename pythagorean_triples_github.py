import math
import itertools

def generate_pythagorean_triples(limit):
    """
    Generates Pythagorean triples (a, b, c) such that a^2 + b^2 = c^2.
    Only considers triples with c <= limit.
    
    Parameters:
    - limit (int): The upper limit for the hypotenuse c.

    Returns:
    - List of tuples: Each tuple represents a Pythagorean triple (a, b, c).
    """
    triples = []
    
    for m in range(1, int(math.sqrt(limit)) + 1):  # m controls the size of the triple
        for n in range(1, m):  # n ensures unique triples
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:  # Coprime and one even-one odd
                # Generate primitive triple
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                
                # Scale the triple to fit within the limit
                k = 1
                while k * c <= limit:
                    triples.append((k * a, k * b, k * c))
                    k += 1

    # Sort and remove duplicates
    triples = sorted(set(triples))
    return triples


def main():
    print("Welcome to the Pythagorean Triple Generator!".center(60))
    
    try:
        limit = int(input("Enter the maximum value for the hypotenuse (c): "))
        if limit < 5:
            print("The limit must be at least 5 to form valid triples.")
            return
        
        triples = generate_pythagorean_triples(limit)
        
        print("\nGenerated Pythagorean Triples:")
        for triple in triples:
            print(f"a = {triple[0]}, b = {triple[1]}, c = {triple[2]}")
        
        print("\nTotal triples found:", len(triples))
    except ValueError:
        print("Invalid input! Please enter a positive integer.")


if __name__ == "__main__":
    main()

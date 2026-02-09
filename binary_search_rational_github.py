# Rational number representation: p / q
class Rational:
    def __init__(self, numerator, denominator):
        self.p = numerator
        self.q = denominator


def compare(a, b):
    """
    Compare two rational numbers a and b
    Returns:
     0  -> equal
     1  -> a > b
    -1  -> a < b
    """
    left = a.p * b.q
    right = a.q * b.p

    if left == right:
        return 0
    return 1 if left > right else -1


def binary_search_rational(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        cmp = compare(arr[mid], target)

        # Found
        if cmp == 0:
            return mid

        # Target is smaller → go left
        if cmp > 0:
            right = mid - 1
        else:
            # Target is larger → go right
            left = mid + 1

    return -1


def main():
    arr = [
        Rational(1, 5),
        Rational(2, 3),
        Rational(3, 2),
        Rational(13, 2)
    ]

    target = Rational(3, 2)

    print(binary_search_rational(arr, target))


if __name__ == "__main__":
    main()

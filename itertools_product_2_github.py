from itertools import product


class CombinationGenerator:
    def __init__(self, first_group, second_group):
        self.first_group = first_group
        self.second_group = second_group

    def generate(self):
        combinations = []

        for pair in product(self.first_group, self.second_group):
            combinations.append(pair)

        return combinations


def main():
    colors = ["Red", "Blue"]
    sizes = ["S", "M", "L"]

    generator = CombinationGenerator(colors, sizes)
    result = generator.generate()

    print("Combinations:")
    for item in result:
        print(item)


if __name__ == "__main__":
    main()
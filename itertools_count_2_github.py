from itertools import count


class SequenceGenerator:
    def __init__(self, start, step, limit):
        self.start = start
        self.step = step
        self.limit = limit  # how many values we want to generate

    def generate(self):
        sequence = []
        counter = count(self.start, self.step)

        for _ in range(self.limit):
            sequence.append(next(counter))

        return sequence


def main():
    start_value = 5
    step_value = 3
    how_many = 6

    generator = SequenceGenerator(start_value, step_value, how_many)
    result = generator.generate()

    print("Generated sequence:", result)


if __name__ == "__main__":
    main()
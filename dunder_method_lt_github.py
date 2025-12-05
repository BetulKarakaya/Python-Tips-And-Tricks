class Resume:
    def __init__(self, candidate: str, score: int):
        self.candidate = candidate
        self.score = score

    def __lt__(self, other):
        """
        Custom sorting rule:
        Higher score → higher priority
        (reverse comparison to get descending order)
        """
        return self.score > other.score

    def __repr__(self):
        return f"{self.candidate} (Score: {self.score})"


class ResumeSorter:
    def __init__(self, resumes: list):
        self.resumes = resumes

    def sort_resumes(self):
        print("\nSorting resumes by candidate score...")
        sorted_list = sorted(self.resumes)
        for r in sorted_list:
            print(" -", r)


def main():
    resumes = [
        Resume("Betül", 92),
        Resume("Alex", 80),
        Resume("John", 75),
        Resume("Emily", 88)
    ]

    sorter = ResumeSorter(resumes)
    sorter.sort_resumes()


if __name__ == "__main__":
    main()

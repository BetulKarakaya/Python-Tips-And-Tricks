class JobOfferAnalyzer:
    def __init__(self, offers: list):
        self.offers = offers

    def get_best_offer(self):
        # Finds the offer with the highest salary
        best_offer = max(self.offers, key=lambda x: x["salary"])
        print(f"Best Offer: {best_offer['role']} with ${best_offer['salary']}")
        return best_offer


def main():
    offers = [
        {"role": "Data Scientist", "salary": 10000},
        {"role": "Data Scientist", "salary": 20000},
        {"role": "Data Engineer", "salary": 15000}
    ]

    analyzer = JobOfferAnalyzer(offers)
    analyzer.get_best_offer()


if __name__ == "__main__":
    main()

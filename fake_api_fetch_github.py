from typing import Callable, Iterable, List, Any, Optional, Iterator
import math

# --- Simulated paginated API for demo purposes ---
def fake_api_fetch(page: int, page_size: int = 5):
    """
    Simulate an API returning (items_on_page, total_count).
    Here we pretend total_count = 23 and items are strings "item-<n>".
    """
    TOTAL = 23
    start = page * page_size
    if start >= TOTAL:
        return [], TOTAL
    end = min(start + page_size, TOTAL)
    items = [f"item-{i}" for i in range(start, end)]
    return items, TOTAL

# --- Paginated container class ---
class PaginatedResults:
    """
    Lazy, iterable container for paginated data with random-access support.

    - __iter__: yields items lazily, fetching pages only when needed.
    - __getitem__: supports index and slice access using cached pages.
    - __len__: returns total number of items (learned from API on first fetch).
    """
    def __init__(self, fetcher: Callable[[int, int], tuple], page_size: int = 5):
        self._fetcher = fetcher
        self.page_size = page_size

        # cache: page_index -> list_of_items
        self._pages: dict[int, List[Any]] = {}
        self._total: Optional[int] = None

    def _ensure_page(self, page_idx: int):
        """Fetch a page if not cached yet, and update total."""
        if page_idx in self._pages:
            return
        items, total = self._fetcher(page_idx, self.page_size)
        self._pages[page_idx] = items
        if self._total is None:
            self._total = total

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate through all items lazily.
        Fetch pages on demand; stop when API returns empty page or we reach total.
        """
        page = 0
        yielded = 0
        # If we already know total, we can compute number of pages; else loop until empty.
        while True:
            self._ensure_page(page)
            page_items = self._pages.get(page, [])
            if not page_items:
                break
            for item in page_items:
                yield item
                yielded += 1
                # stop early if we know total and yielded reached it
                if self._total is not None and yielded >= self._total:
                    return
            page += 1

    def __len__(self) -> int:
        """Return total items. Triggers a fetch of first page if unknown."""
        if self._total is None:
            # ensure at least page 0 is fetched to learn total
            self._ensure_page(0)
        return self._total or 0

    def __getitem__(self, index):
        """
        Support integer index and slices.
        For integer: fetch necessary page, return cached value or raise IndexError.
        For slice: return a list built by fetching only needed pages.
        """
        if isinstance(index, slice):
            # normalize slice
            start, stop, step = index.indices(len(self))
            if step == 1:
                # efficient contiguous slice
                return [self[i] for i in range(start, stop)]
            else:
                return [self[i] for i in range(start, stop, step)]

        # integer index
        if index < 0:
            # support negative indexing by translating
            total = len(self)
            index = total + index
        if index < 0:
            raise IndexError("Index out of range")

        page_idx = index // self.page_size
        inner_idx = index % self.page_size

        # fetch required page(s)
        self._ensure_page(page_idx)
        page = self._pages.get(page_idx, [])
        if inner_idx >= len(page):
            # may be out of range (e.g., last partial page)
            raise IndexError("Index out of range")
        return page[inner_idx]

# --- Demo usage ---
def main():
    results = PaginatedResults(fake_api_fetch, page_size=5)

    print("Total items (len):", len(results))
    print("\nIterating (first 8 items):")
    for i, it in enumerate(results):
        if i >= 8:
            break
        print(" ", i, it)

    print("\nRandom access examples:")
    print(" item at index 0:", results[0])
    print(" item at index 7:", results[7])
    print(" last item (negative index):", results[-1])

    print("\nSlice example (5:10):", results[5:10])

if __name__ == "__main__":
    main()

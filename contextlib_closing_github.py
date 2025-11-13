from contextlib import closing
import random
import time

class DataStream:
    """Simulates a live data stream that MUST be closed properly."""
    
    def __init__(self):
        self.active = True
        print("🔵 Stream opened.")

    def __iter__(self):
        return self._generator()

    def _generator(self):
        """Fake live stream producing values."""
        while self.active:
            yield random.randint(1, 100)
            time.sleep(0.2)

    def close(self):
        """Properly terminate the stream."""
        self.active = False
        print("🔴 Stream closed safely!")


class StreamReader:
    """Reads a few items from the stream using contextlib.closing."""
    
    def __init__(self, stream: DataStream):
        self.stream = stream

    def read_n(self, count=5):
        with closing(self.stream):   # ensures .close() is called automatically
            for i, value in zip(range(count), self.stream):
                print(f"-- Received: {value}")


def main():
    stream = DataStream()
    reader = StreamReader(stream)
    reader.read_n(5)

if __name__ == "__main__":
    main()

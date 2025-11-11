import asyncio
import time
from contextlib import asynccontextmanager

class AsyncTimer:
    """A reusable async context manager & decorator that times async operations."""
    def __init__(self, task_name: str):
        self.task_name = task_name
        self.start = None

    async def __aenter__(self):
        self.start = time.perf_counter()
        print(f"🟢 Started: {self.task_name}")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(f"🔴 Finished: {self.task_name} (⏳ {elapsed:.4f}s)\n")
        return False  # don't suppress exceptions

    def __call__(self, func):
        async def wrapper(*args, **kwargs):
            async with self:
                return await func(*args, **kwargs)
        return wrapper


# Example async function using decorator
@AsyncTimer("Simulated API Request")
async def fetch_data():
    print("- Fetching data from API...")
    await asyncio.sleep(1.5)
    print("- Data fetched successfully!")


async def main():
    # Used as decorator
    await fetch_data()

    # Used as async context manager
    async with AsyncTimer("Data Processing"):
        await asyncio.sleep(1)
        print("- Processing data... done!")


if __name__ == "__main__":
    asyncio.run(main())

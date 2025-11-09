import weakref
import gc

class ImageCache:
    """Stores image objects without preventing garbage collection."""
    def __init__(self):
        self.cache = weakref.WeakValueDictionary()

    def add_image(self, name, image_obj):
        self.cache[name] = image_obj
        print(f"- Added '{name}' to cache.")

    def show_cache(self):
        print("-- Current cache keys:", list(self.cache.keys()) or "Empty")

class Image:
    """Dummy image class for demonstration."""
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"<Image: {self.name}>"

def main():
    manager = ImageCache()

    img1 = Image("sunrise.png")
    img2 = Image("forest.jpg")

    manager.add_image("morning", img1)
    manager.add_image("nature", img2)

    manager.show_cache()

    # Delete one reference
    del img1
    gc.collect()  # Force garbage collection

    print("\nAfter garbage collection:")
    manager.show_cache()

if __name__ == "__main__":
    main()

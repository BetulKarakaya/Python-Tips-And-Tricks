if __name__ == "__main__":
    # Bir dizenin belirli bir karakterle başlayıp başlamadığını veya bitip bitmediğini kontrol eder
    text1 = "Hello World!"
    text2 = "Hello World! It's me, Betül"

    print(text1.startswith("Hello"))  # Output: True
    print(text1.endswith("World!"))    # Output: True
    print(text1.endswith("World"))    # Output: False

    print(text2.startswith("Hello"))  # Output: True
    print(text2.endswith("Betül"))    # Output: True
    print(text2.endswith("betül"))    # Output: False

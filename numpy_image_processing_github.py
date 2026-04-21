import numpy as np

class ImageProcessor:
    """
    A class to treat images as raw 3D NumPy matrices 
    for high-speed pixel manipulation.
    """
    def __init__(self, height=100, width=100):
        # Create a "dummy" RGB image (Random noise)
        # Shape: (Height, Width, 3 Channels)
        self.image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    def __str__(self):
        return f"Image Matrix: {self.image.shape[0]}x{self.image.shape[1]} pixels."

    def apply_filters(self):
        """
        TRICK: Array Slicing and Vectorized Arithmetic.
        We manipulate the RGB channels independently using matrix slicing.
        """
        # 1. Channel Isolation: Zero out the Green and Blue channels
        # [all rows, all columns, index 0(Red)]
        red_only = self.image.copy()
        red_only[:, :, [1, 2]] = 0 

        # 2. Brightness Boost: Scalar Addition (Broadcasting)
        # We cap the values at 255 using np.clip to prevent "rollover"
        bright_image = np.clip(self.image.astype(np.int16) + 50, 0, 255).astype(np.uint8)

        # 3. Grayscale Conversion: Weighted Average
        # Multiply RGB by standard weights and sum along the last axis
        weights = [0.2989, 0.5870, 0.1140]
        grayscale = np.dot(self.image, weights).astype(np.uint8)

        return red_only, bright_image, grayscale

def main():
    # 1. Initialize a 1080p-style matrix
    proc = ImageProcessor(height=1080, width=1920)
    print(proc)

    # 2. Process
    red_img, bright_img, gray_img = proc.apply_filters()

    # 3. Check Results
    print("\n--- Matrix Processing Complete ---")
    print(f"Red Channel Matrix Mean: {np.mean(red_img):.2f}")
    print(f"Grayscale Matrix Shape: {gray_img.shape}")

if __name__ == "__main__":
    main()
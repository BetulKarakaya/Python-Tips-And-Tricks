import numpy as np
from scipy.io import wavfile  # Standard library for audio I/O

class SignalGenerator:
    """
    A class to generate complex wave signals and export them as audio.
    """
    def __init__(self, duration_sec, sample_rate=44100):
        self.sample_rate = sample_rate
        self.t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), endpoint=False)

    def generate_chord(self, frequencies):
        # Broadcasting: (N, 1) frequencies against (M,) time samples
        freqs = np.array(frequencies).reshape(-1, 1)
        waves = np.sin(2 * np.pi * freqs * self.t)
        
        # Superposition: Merging waves into one signal
        combined_signal = np.sum(waves, axis=0)
        
        # Peak Normalization: Prevents digital clipping
        return combined_signal / np.max(np.abs(combined_signal))

    def save_to_wav(self, signal, filename="output.wav"):
        """
        TRICK: Bit-Depth Scaling.
        WAV files (PCM_16) require values between -32768 and 32767.
        """
        # Convert [-1.0, 1.0] float to 16-bit signed integer
        audio_data = (signal * 32767).astype(np.int16)
        
        # Write to disk
        wavfile.write(filename, self.sample_rate, audio_data)
        print(f"Successfully recorded: {filename}")

def main():
    # 1. Initialize (Longer duration to actually hear it)
    synth = SignalGenerator(duration_sec=2.0)
    
    # 2. C-Major frequencies
    c_major = [261.63, 329.63, 392.00]
    
    # 3. Generate and Save
    signal = synth.generate_chord(c_major)
    synth.save_to_wav(signal, "c_major_chord.wav")

if __name__ == "__main__":
    main()
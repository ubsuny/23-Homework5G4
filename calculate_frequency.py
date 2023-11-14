import numpy as np
#import pandas as pd
def calculate_frequencies(fft_output, sampling_rate):
    N = len(fft_output)
    frequencies = np.fft.fftfreq(N, d=1/sampling_rate)
    return frequencies
def find_peak_frequency(fft_output, sampling_rate):
    frequencies = calculate_frequencies(fft_output, sampling_rate)
    positive_frequencies = frequencies[:len(frequencies)//2]
    magnitude_spectrum = np.abs(fft_output[:len(fft_output)//2])
# Find the index of the maximum amplitude
    peak_index = np.argmax(magnitude_spectrum)
# Get the corresponding frequency
    peak_frequency = positive_frequencies[peak_index]

    return peak_frequency


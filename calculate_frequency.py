import numpy as np
import pandas as pd
def calculate_frequencies(fft_output, sampling_rate):
    N = len(fft_output)
    frequencies = np.fft.fftfreq(N, d=1/sampling_rate)
    return frequencies

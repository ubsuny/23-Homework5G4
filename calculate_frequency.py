import numpy as np

def calculate_frequencies(fft_output, sampling_rate):
    """
    Calculate the frequencies corresponding to the FFT output.

    Parameters:
    - fft_output (array-like): The output of the FFT.
    - sampling_rate (float): The sampling rate of the input data.

    Returns:
    - array-like: Frequencies corresponding to the FFT output.
    """
    N = len(fft_output)
    frequencies = np.fft.fftfreq(N, d=1/sampling_rate)
    return frequencies

def find_peak_frequency(fft_output, sampling_rate):
    """
    Find the peak frequency from the FFT output.

    Parameters:
    - fft_output (array-like): The output of the FFT.
    - sampling_rate (float): The sampling rate of the input data.

    Returns:
    - float: The peak frequency.
    """
    frequencies = calculate_frequencies(fft_output, sampling_rate)
    positive_frequencies = frequencies[:len(frequencies)//2]
    magnitude_spectrum = np.abs(fft_output[:len(fft_output)//2])
    
    # Find the index of the maximum amplitude
    peak_index = np.argmax(magnitude_spectrum)
    
    # Get the corresponding frequency
    peak_frequency = positive_frequencies[peak_index]

    return peak_frequency

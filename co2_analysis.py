import numpy as np
import scipy.signal as signal
import pandas as pd

def fft(x):
    """
    Parameters
    ----------
    x : array_like
        A complex data vector of length N

    Returns
    -------
    array_like
        A complex vector of the same length as x containing the FFT coefficients
    """
    N = len(x)
    if N <= 1:
        return x
    elif N % 2 == 1:  # N is odd, fall back to discrete transform
        print('N is ' + str(N) + ', fall back to discrete transform')
        return discrete_transform(x)
    even = fft(x[0::2])
    odd = fft(x[1::2])
    return np.array([even[k] + np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)] +
                    [even[k] - np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)])

def discrete_transform(data):
    """
    Parameters
    ----------
    data : array_like
        A complex data vector of length N

    Returns
    -------
    array_like
        A complex vector of the same length as x containing the FFT coefficients
    """
    N = len(data)
    transform = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for j in range(N):
            angle = 2 * np.pi * k * j / N
            transform[k] += data[j] * np.exp(1j * angle)
    return transform
    

def find_peak_frequency(X):
    """
    Parameters
    ----------
    X : array_like
        A real data vector representing a signal

    Returns
    -------
    int
        The number of peaks in the frequency spectrum of the signal
    """
    Y = fft(X)
    N = len(Y)
    half = N // 2
    abs_Y = np.abs(Y[:half])
    peak_indices = signal.argrelextrema(abs_Y, np.greater)[0]
    number_of_peaks = len(peak_indices)
    return number_of_peaks


def calculate_frequency(data, sampling_rate):
    """
    Parameters
    ----------
    data : array_like
        Time-series data for CO2 concentrations.
    sampling_rate : int
        Sampling rate of the data.

    Returns
    -------
    float
        Frequency of the CO2 signal.
    """
    N = len(data)
    time_interval = 1 / sampling_rate
    frequency = np.fft.fftfreq(N, time_interval)
    return frequency


def calculate_peak_frequency(data, sampling_rate):
    """
    Parameters
    ----------
    data : array_like
        Time-series data for CO2 concentrations.
    sampling_rate : int
        Sampling rate of the data.

    Returns
    -------
    float
        Peak frequency of the CO2 signal.
    """
    frequency = calculate_frequency(data, sampling_rate)
    Y = np.fft.fft(data)
    half = len(Y) // 2
    abs_Y = np.abs(Y[:half])
    peak_index = np.argmax(abs_Y)
    peak_frequency = frequency[peak_index]
    return peak_frequency

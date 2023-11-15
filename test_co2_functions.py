import numpy as np
from co2_analysis import calculate_frequency, calculate_peak_frequency, find_peak_frequency

def test_calculate_frequency():
    data = np.array([1, 2, 3, 4, 5])
    sampling_rate = 1
    assert calculate_frequency(data, sampling_rate)[0] == 0.0

def test_calculate_peak_frequency():
    data = np.array([1, 2, 3, 4, 5])
    sampling_rate = 1
    assert calculate_peak_frequency(data, sampling_rate) == 0.0

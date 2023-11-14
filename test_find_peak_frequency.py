import numpy as np
import pytest
from calculate_frequency import find_peak_frequency

@pytest.fixture
def sample_data():
    # Generate sample data for testing
    sampling_rate = 1000  # Example sampling rate
    time_duration = 1.0  # Example time duration in seconds
    time_values = np.arange(0, time_duration, 1/sampling_rate)
    signal = np.sin(2 * np.pi * 50 * time_values)  # Example signal with frequency of 50 Hz
    fft_output = np.fft.fft(signal)
    
    return fft_output, sampling_rate

def test_find_peak_frequency(sample_data):
    fft_output, sampling_rate = sample_data
    peak_frequency = find_peak_frequency(fft_output, sampling_rate)
    
    assert isinstance(peak_frequency, float)
    assert 0 <= peak_frequency <= sampling_rate/2

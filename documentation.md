# FFT

The Fast Fourier Transform (FFT) is an algorithm for computing the Discrete Fourier Transform (DFT) and its inverse. The DFT is a mathematical transformation that converts a sequence of complex numbers (such as a signal in the time domain) into another sequence of complex numbers (its representation in the frequency domain).

# Data source:
We have taken the FFT of CO2/methane data of the most recent monthly average CO2 data. 
https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_bme_surface-flask_1_ccgg_month.txt 
# Preparing the data for taking FFT
We imported the data station by using pandas. Next, we used the code below:

# df['date'] = pd.to_datetime(df[['year','month']].assign(day=1)).dt.to_period('M') 
This code takes the 'year' and 'month' columns from the DataFrame, adds a 'day' column with a constant value of 1, converts these three columns into a datetime object, and then converts that datetime object into a period object representing months. The result is stored in a new 'date' column in the original DataFrame.
The plot is given below
<img width="619" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/7870893c-ff6a-4a12-8c38-972753bb8eb7">
# Taking FFT
We used the code below:

def discrete_transform(data):
    """Return Discrete Fourier Transform (DFT) of a complex data vector"""
    N = len(data)
    transform = np.zeros(N)
    for k in range(N):
        for j in range(N):
            angle = 2 * np.pi * k * j / N
            transform[k] += data[j] * np.exp(1j * angle)
    return transform

def fft(x):
    N = len(x)
    if N <= 1: return x
    elif N % 2 == 1:         # N is odd, lemma does not apply
        print ('N is ' + str(N) + ', fall back to discrete transform')
        return discrete_transform(x)
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    return np.array( [even[k] + np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)] + \
                     [even[k] - np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)] )

The code uses recursion to efficiently compute the FFT. It divides the problem into smaller subproblems and then combines the results, reducing the overall complexity compared to the straightforward DFT computation. The algorithm takes advantage of the periodicity and symmetry properties of the Fourier transform to achieve a faster computation.

# X= fft(df['value'][-512:])
This line of code is computing the FFT of the most recent 512 values in the 'value' column of your DataFrame df, and the result is stored in the variable X. The FFT will provide a representation of the frequency components present in the time series data. This operation is often used in signal processing and time series analysis to analyze the frequency content of a signal.

# Plot of FFT of Monthly Average CO2 Concentration

<img width="500" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/aa7a6640-4ac9-4de7-a663-79ba47fcdb65">

# The function that calculates the actual frequency in useful units:

We used the code below
<img width="556" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/8ee29c64-53d1-4a6b-81e4-ee3ee8141256">

This code segment calculates the FFT of the last 512 values in the 'value' column, computes the corresponding frequencies, and then plots the frequency spectrum using Matplotlib with a logarithmic y-scale for better visibility of amplitudes. The resulting plot provides insights into the frequency components present in the time series data.

<img width="593" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/0dc544c2-5c3f-452c-a5b7-1b932dd4455e">

# Padding and windowing the data:
We used the code below:

<img width="508" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/5ae67886-251f-4182-9b45-05abc1e90ef5">


# Padding
This code ensures that the length of the 'value' column (y) is a power of 2 by padding it with zeros if necessary. This operation may be useful in the context of algorithms or computations that are optimized for inputs with a length that is a power of 2, such as some FFT (Fast Fourier Transform) implementations.

# Windowing
The code applies a Hann window to the time series data represented by the 'value' column in the DataFrame df. The Hann window is a type of tapering function often used in signal processing to reduce spectral leakage when performing operations like the Fast Fourier Transform (FFT). It gradually reduces the amplitude of data points toward the edges, smoothing the data and minimizing artifacts introduced by abrupt transitions at the edges of the signal.


# Plot FFT after applying Hann window:
<img width="326" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/c8787007-5c93-4bab-8a30-1bf611ac1d7f">

the code applies the FFT to the time series data after applying a Hann window, calculates the power spectrum, and then plots the result on a logarithmic scale. This visualization helps analyze the frequency content of the signal, particularly emphasizing lower-amplitude components.

<img width="432" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/9f853269-57ff-401a-b496-7661c33b5d09">

# Inverse FFT
<img width="334" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/9ba82c6d-b549-44d7-a6d1-e0eeb3b14f57">
the code visualizes the frequency content of both the original and filtered signals in the time domain after applying a filtering operation in the frequency domain using the FFT and IFFT. The logarithmic scale on the y-axis is often used to emphasize lower-amplitude components.

# Plot of filtered and raw data
<img width="529" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/ad8ad94f-995e-404a-8a9a-48cfe35eb608">
















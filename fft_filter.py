import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


# reading in data
df = pd.read_csv('https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_bme_surface-flask_1_ccgg_month.txt',
    delimiter="\s+",skiprows=54, names=['site',	'year',	'month',	'value'])
df['date'] = pd.to_datetime(df[['year','month']].assign(day=1)).dt.to_period('M')
df=df.set_index(df['date'])

# settings original values for graphing later.
y_original = df['value'].copy()
N_orginal = len(y_original)

# fourier transfrom function
def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    return np.array( [even[k] + np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)] + \
                     [even[k] - np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)] )

# defining the inverse fourier transform function
def ifft(x) :
    from numpy import conj, divide

    # conjugate the complex numbers
    x = np.conj(x)

    # forward fft
    X = fft( x );

    # conjugate the complex numbers again
    X = np.conj(X)

    # scale the numbers
    X = X / len(X)

    return X

df['months'] = [m.n for m in (df.index-df.index[0])]  # creating new months colummn

# Padding data

y = df['value']
N = len(y)
log2N = math.log(N,2)
next_pow_of_2 = int(log2N) + 1
if log2N - int(log2N) > 0.0 :
    ypads = np.full( 2**( next_pow_of_2) - N, 0, dtype=np.double)
    y = np.concatenate( (y, ypads) )
x = np.arange(len(y))
N = len(y)

# Windowing
window = 2 - 1 * np.cos(2 * np.pi * x / (len(y) - 1))
y_window = y * window
Y = fft(y_window)

# Filtering



Y_abs = abs(Y) # absolute value

# Inverse FFT
y_filtered = ifft(Y)
y_filtered_abs= abs(y_filtered)

# reversing window and padding
y_filtered_unwindow = (y_filtered / window)
y_new = y_filtered_unwindow[:237]

# reversing window and padding
y_filtered_unwindow = (y_filtered / window)
y_new = y_filtered_unwindow[:237]

# making new column
df['value_clean'] = y_new

# plotting the data
y_original.plot(label = "raw")
df['value_clean'].plot(label = "clean", linestyle='dashed')

plt.title("raw/clean data comparison")  # Title of the plot
plt.legend()
plt.show()

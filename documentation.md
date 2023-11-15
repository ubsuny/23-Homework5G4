# FFT

The Fast Fourier Transform (FFT) is an algorithm for computing the Discrete Fourier Transform (DFT) and its inverse. The DFT is a mathematical transformation that converts a sequence of complex numbers (such as a signal in the time domain) into another sequence of complex numbers (its representation in the frequency domain).

# Data source:
We have taken the FFT of CO2/methane data of the most recent monthly average CO2 data. 
https://gml.noaa.gov/aftp/data/trace_gases/co2/flask/surface/txt/co2_bme_surface-flask_1_ccgg_month.txt 
# Preparing the data for taking FFT
We imported the data station by using pandas. Next, we used the code below
df['date'] = pd.to_datetime(df[['year','month']].assign(day=1)).dt.to_period('M') 
This code takes the 'year' and 'month' columns from the DataFrame, adds a 'day' column with a constant value of 1, converts these three columns into a datetime object, and then converts that datetime object into a period object representing months. The result is stored in a new 'date' column in the original DataFrame.
The plot is given below
<img width="619" alt="image" src="https://github.com/sharmistharanit/23-Homework5G4/assets/143737948/7870893c-ff6a-4a12-8c38-972753bb8eb7">







import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import *

plt.style.use('default')

data=pd.read_csv("levelhmi.csv")
data["Time"]=pd.to_datetime(data["Time"])
data=data.set_index("Time")
data=data["Level"]

sns.set_style('whitegrid')
plot(x='column1', y='column2', data=data)

plt.show
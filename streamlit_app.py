import pandas as pd
import numpy as np


df = pd.read_excel(
	io='C:/Users/matthf8/OneDrive - kochind.com/Desktop/NBAtool.xlsx',
	sheet_name='Consolidated')

st.dataframe(data=df)
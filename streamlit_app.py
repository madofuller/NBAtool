import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA Tool')


df = pd.read_excel('NBA_Tool.xlsx', sheet_name='Consolidated')

st.dataframe(data=df)


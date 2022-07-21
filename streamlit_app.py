import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA Tool')

df = pd.read_excel('NBA_Tool.xlsx', 

	sheet_name='Consolidated')

product = df['Product'].drop_duplicates(), df['Product'].dropna()

site = df['Location'].drop_duplicates(), df['Location'].dropna()

contract = df['Contract_Index'].drop_duplicates(), df['Contract_Index'].dropna()

with st.sidebar:
	product_choice = st.selectbox(
	'Choose Product', product)
	site_choice = st.selectbox(
	'Choose Site Location', site)
	contract_choice = st.selectbox(
	'Choose Contract', contract)
	date_choice = st.date_input(
    "Choose Date")




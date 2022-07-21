import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA Tool')

df = pd.read_excel('NBA_Tool.xlsx', 

	sheet_name='Consolidated')

product = df['Product'].drop_duplicates()

site = df['Location'].drop_duplicates()

contract = df['Contract_Index'].drop_duplicates()

with st.sidebar:
	product_choice = st.selectbox(
	'Choose Product', options=['select']+list(df.keys())
	site_choice = st.selectbox(
	'Choose Site Location', options=df[product_choice])
	contract_choice = st.selectbox(
	'Choose Contract', contract)
	date_choice = st.date_input(
    "Choose Date")

st.write(product_choice, site_choice, contract_choice, date_choice)


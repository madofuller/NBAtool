import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA Tool')

df = pd.read_excel('NBA_Tool.xlsx', 

	sheet_name='Consolidated')

product = df['Product'].drop_duplicates()

site = df['Location'].drop_duplicates()

vc = df['Variable Costs'].dropna()

contract = df['Contract_Index'].dropna()

with st.sidebar:
	product_choice = st.selectbox(
	'Choose Product', product)
	site_choice = st.selectbox(
	'Choose Site Location', site)
	contract_choice = st.selectbox(
	'Choose Contract', contract)
	vc_choice = st.selectbox(
	'Choose Shipping Location', vc)
	date_choice = st.date_input(
    "Choose Date")

st.write(product_choice, site_choice, contract_choice, date_choice)


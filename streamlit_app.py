import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA Tool')

df = pd.read_excel('NBA_Tool.xlsx', sheet_name='Consolidated')

product = df['Product'].drop_duplicates()

site = df['Location'].drop_duplicates()

contract = df['Contract_Index'].drop_duplicates()


with st.sidebar:
	product_choice = st.selectbox(
		'Choose Product', product)
	if 'AA' in product_choice:
		st.write('AA selected')
	site_choice = st.selectbox(
		'Choose Site Location', site)
	contract_choice = st.selectbox(
		'Choose Contract',
		(contract))
	date_choice = st.date_input(
    	"Choose Date")


st.dataframe(data=df)


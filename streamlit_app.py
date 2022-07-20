import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA Tool')

df = pd.read_excel('NBA_Tool.xlsx', sheet_name='Consolidated')

product = df['Product'].drop_duplicates()







with st.sidebar:
	product_choice = st.selectbox(
		'Choose Product',
		('AA', 'HMD', 'ADN', 'Polymer'))
	site_choice = st.selectbox(
		'Choose Site Location',
		('North America', 'China', 'Rest of Asia'))
	customer_choice = st.selectbox(
		'Choose Customer',
		('North America', 'China', 'Rest of Asia'))
	contract_choice = st.selectbox(
		'Choose Contract',
		('North America', 'China', 'Rest of Asia'))
	date_choice = st.date_input(
    	"Choose Date")


st.dataframe(data=df)


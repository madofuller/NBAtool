import streamlit as st
import pandas as pd
import numpy as np

st.title('NBA Tool')

with st.sidebar:
	product = st.selectbox(
		'Choose Product',
		('AA', 'HMD', 'ADN', 'Polymer'))
	site = st.selectbox(
		'Choose Site Location',
		('North America', 'China', 'Rest of Asia'))
	customer = st.selectbox(
		'Choose Customer',
		('North America', 'China', 'Rest of Asia'))
	contract = st.selectbox(
		'Choose Contract',
		('North America', 'China', 'Rest of Asia'))
	choose_date = st.date_input(
    	"Choose Date")
	choose_customer

df = pd.read_excel('NBA_Tool.xlsx', sheet_name='Consolidated')

st.dataframe(data=df)


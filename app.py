import streamlit as st 
import pandas as pd 
from bs4 import BeautifulSoup
import requests

URL = 'https://www.fdic.gov/resources/bankers/national-rates/index.html'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

date =soup.find('p', class_='font-sans-md tablet:font-sans-xs text-italic text-center tablet:padding-x-10 margin-bottom-4')

st.set_page_config(layout="wide")

st.write("Note: This is not a financial advice. Please consult your financial advisor before making any investment decisions.")

st.title("FDIC National Rates")

table = soup.find('table', class_='fdic-table fdic-table-alt width-full')

# put table into a dataframe

df = pd.read_html(str(table))[0]

st.dataframe(df)

st.write("Source: FDIC")

st.write("Data last updated:",date.getText())



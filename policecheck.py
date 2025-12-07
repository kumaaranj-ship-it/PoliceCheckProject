import streamlit as st
import pandas as pd

file_path = "traffic_stops.xlsx"
df = pd.read_excel(file_path)

df.head()
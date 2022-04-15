import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.title('**Streamlit Components**')
st.write('*Components are third-party Python modules that extend what\'s possible with Streamlit and they are just a pip-install away!*')


st.subheader('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# Generates report
pr = df.profile_report()
st_profile_report(pr)


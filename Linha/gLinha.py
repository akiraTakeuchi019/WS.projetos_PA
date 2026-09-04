# Desculpa pedro (Exeto o eiji que não ligo E especialmente vsf cebolinha)

import streamlit as st;
import pandas as pd;

data= {
    'produto': ['produto A', 'produto B' ,'produto C' ,'produto D'],
    'venda':   [150,200,300,350]
}

df= pd.DataFrame(data)
st.line_chart(df.set_index('produto'))

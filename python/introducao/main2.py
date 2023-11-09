import streamlit as st

st.markdown("# Calculo de area:")

altura = st.slider("Altura: ")
base = st.slider("Base: ")

area = (base*altura)/2

st.write(area)

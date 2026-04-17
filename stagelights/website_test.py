from lotus_lamp import LotusLamp
import streamlit as st
import asyncio

st.header("Input Elements")

st.subheader("Light Options")

button_clicked = st.button("Test")

if button_clicked:
    print("Success")

st.divider()


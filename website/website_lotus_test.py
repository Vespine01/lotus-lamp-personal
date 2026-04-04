from lotus_control import red
from lotus_control import blue
from lotus_control import green
import streamlit as st

st.header("Back Stage Light Options")

option_red = st.button("Red")
option_blue = st.button("Blue")
option_green = st.button("Green")

if option_red:
    asyncio.run(red())

if option_blue:
    asyncio.run(blue())

if option_green:
    asyncio.run(green())



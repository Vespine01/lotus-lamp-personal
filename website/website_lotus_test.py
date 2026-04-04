from lotus_control import red, blue, green, white, yellow, purple, orange, pink, cyan, off
import streamlit as st
import asyncio

st.header("Back Stage Light Options")

option_red = st.button("Red")
option_blue = st.button("Blue")
option_green = st.button("Green")
option_white = st.button("White")
option_yellow = st.button("Yellow")
option_purple = st.button("Purple")
option_orange = st.button("Orange")
option_pink = st.button("Pink")
option_cyan = st.button("Cyan")
option_off = st.button("Off")

if option_red:
    asyncio.run(red())

if option_blue:
    asyncio.run(blue())

if option_green:
    asyncio.run(green())

if option_white:
    asyncio.run(white())

if option_yellow:
    asyncio.run(yellow())

if option_purple:
    asyncio.run(purple())

if option_orange:
    asyncio.run(orange())

if option_pink:
    asyncio.run(pink())

if option_cyan:
    asyncio.run(cyan())
    
if option_off:
    asyncio.run(off())



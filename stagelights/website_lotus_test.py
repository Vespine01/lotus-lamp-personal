import lotus_control
import streamlit as st
import asyncio

st.header("Back Stage Light Options")


if st.button("Red"):
    asyncio.run(lotus_control.red())

if st.button("Blue"):
    asyncio.run(lotus_control.blue())

if st.button("Green"):
    asyncio.run(lotus_control.green())

if st.button("White"):
    asyncio.run(lotus_control.white())

if st.button("Yellow"):
    asyncio.run(lotus_control.yellow())

if st.button("Purple"):
    asyncio.run(lotus_control.purple())

if st.button("Orange"):
    asyncio.run(lotus_control.orange())

if st.button("Pink"):
    asyncio.run(lotus_control.pink())

if st.button("Cyan"):
    asyncio.run(lotus_control.cyan())

if st.button("Off"):
    asyncio.run(lotus_control.off())


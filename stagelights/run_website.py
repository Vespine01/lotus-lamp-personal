import lotus_control
import streamlit as st
import asyncio
import stagelight_connection

print("Connecting to stagelights...")
asyncio.run(stagelight_connection.connect_lamps())

if not stagelight_connection.connected:
    st.error("Failed to connect to any lamps. Please check Connection Log and try again.")

else:
    print("Starting Stagelights Web Interface...")

    st.header("Stage Light Options")

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


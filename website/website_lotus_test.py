from lotus_control import main
import streamlit as st

st.header("Input Elements")

st.subheader("Light Options")

button_clicked = st.button("Test")

if button_clicked:
    asyncio.run(main())

st.divider()


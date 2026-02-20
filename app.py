import streamlit as st

st.set_page_config(page_title="Happy Python Day", page_icon="🐍")

st.title("🐍 Happy Python Day")
st.write("Celebrating the Spirit of Python")

st.divider()

name = st.text_input("Enter your name")

if st.button("Enter"):
    if name:
        st.success(f"""
🎉 Thank you, {name}!

Today we celebrate not just Python,
but the amazing learners and developers who bring it to life.

Your dedication and passion keep the spirit of coding alive.

Keep innovating. Keep building. Keep inspiring. 🐍✨
""")
    else:
        st.warning("Please enter your name")

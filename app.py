import streamlit as st
import google.generativeai as genai #type ignore

# Setup Gemini using your Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Viral Scan PRO")
st.write("App is now running.")


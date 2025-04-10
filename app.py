import streamlit as st
from frontend.ui import render_ui
from backend.processor import process_resume

st.set_page_config(page_title="📑 ATS Resume Checker (Gemma 3 via Ollama)", layout="centered")
st.title("📑 ATS Resume Checker with **Gemma 3** 🔍")

resume_file, job_description, submit = render_ui()

if submit and resume_file and job_description:
    with st.spinner("Analyzing with Gemma 3 model..."):
        feedback = process_resume(resume_file, job_description)
        st.subheader("✅ ATS Feedback")
        st.markdown(feedback)
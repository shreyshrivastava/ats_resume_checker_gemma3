import requests
from utils.pdf_reader import extract_text_from_pdf
import streamlit as st

def process_resume(resume_file, job_description):
    resume_text = extract_text_from_pdf(resume_file)
    prompt = f"""
You are a smart ATS resume analyzer powered by Gemma 3.

Job Description:
{job_description}

Candidate Resume:
{resume_text}

Provide a short ATS-style match report:
1. Skills matched
2. Missing qualifications or gaps
3. Suggestions to improve the resume
4. Overall ATS match score (0-100)
"""

    try:
        response = requests.post(
            f"{st.session_state.ollama_host}/api/generate",
            json={
                "model": st.session_state.ollama_model,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json().get("response", "No response received.")
    except requests.exceptions.RequestException as e:
        return f"❌ Error connecting to Ollama: {e}"
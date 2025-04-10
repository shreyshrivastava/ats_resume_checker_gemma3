import streamlit as st

def render_ui():
    with st.sidebar:
        st.header("⚙️ Settings")
        st.markdown("Using **Gemma 3 via Ollama** 🧠")
        ollama_model = st.text_input("🧠 Ollama Model", value="gemma:latest")
        ollama_host = st.text_input("🌐 Ollama Host", value="http://localhost:11434")

    st.markdown("---")
    resume_file = st.file_uploader("📄 Upload Resume (PDF)", type="pdf")
    job_description = st.text_area("📋 Paste Job Description", height=200)
    submit = st.button("📝 Get ATS Feedback")

    # Save to session
    st.session_state.ollama_model = ollama_model
    st.session_state.ollama_host = ollama_host

    return resume_file, job_description, submit
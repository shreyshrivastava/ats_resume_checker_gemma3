# ATS Resume Checker with Gemma 3 (via Ollama) 🚀

This Streamlit app allows you to upload your resume and a job description to get an ATS (Applicant Tracking System) match analysis using **Gemma 3**, running locally via **Ollama**.

---

## 💡 How It Works

- 🧠 Powered by [Ollama](https://ollama.com/) running the `gemma` model locally
- 📄 Upload your resume as a PDF
- 📋 Paste a job description
- 🔍 Get real-time feedback using **Gemma 3**

---

## ⚙️ Prerequisites

### 1. Install Ollama

Ollama is a local LLM runner. Download and install it:

```bash
https://ollama.com/download
```

After installation, make sure it's running:
```bash
ollama serve
```

### 2. Pull the Gemma 3 Model

Once Ollama is running:

```bash
ollama pull gemma
```

> You can also use other models like `gemma:7b` or `gemma:latest`.

---

## 🚀 Run the App

### 1. Clone or download this repo

```bash
unzip ats_resume_checker_gemma3.zip
cd ats_resume_checker_gemma3
```

### 2. Install dependencies

We recommend using a virtual environment.

```bash
pip install -r requirements.txt
```

### 3. Start the App

```bash
streamlit run app.py
```

---

## 🧠 Model Settings (Optional)

You can change these in the sidebar of the app:

- **Ollama Host**: Default is `http://localhost:11434`
- **Ollama Model**: Default is `gemma:latest`

---

## 🔒 Privacy Note

All processing is done locally. Your resume and job description are **never uploaded to the cloud**. You are in full control.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Ollama (Local LLM runtime)
- Gemma 3 (LLM)
- PyMuPDF (PDF parsing)

---

## 📸 Screenshot
\![image](https://github.com/user-attachments/assets/8f88faba-9cdc-4afe-a5b8-a9f154b526be)


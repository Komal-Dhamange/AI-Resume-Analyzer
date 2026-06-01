import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from groq import Groq

# ---------------------------------
# INITIAL SETUP & CONFIG
# ---------------------------------
st.set_page_config(layout="wide")
client = Groq(api_key="YOUR API KEY")

# Initialize Session State
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'users' not in st.session_state:
    st.session_state['users'] = {"admin": "password123"} # Default user

# ---------------------------------
# FUNCTIONS
# ---------------------------------
def extract_pdf_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_docx_text(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ---------------------------------
# MAIN APP LOGIC
# ---------------------------------
def show_main_app():
    st.title("AI Resume Analyzer (Groq + Llama3) 🚀")
    
    # Sidebar for History
    st.sidebar.title("History")
    for i, hist in enumerate(st.session_state['history']):
        if st.sidebar.button(f"Resume {i+1}", key=f"hist_{i}"):
            st.write("---")
            st.write(hist)
    
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()

    uploaded_file = st.file_uploader("Upload Resume (PDF / DOCX / TXT)", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            resume_text = extract_pdf_text(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_docx_text(uploaded_file)
        else:
            resume_text = uploaded_file.read().decode("utf-8")

        st.subheader("Resume Content")
        st.text_area("Extracted Text", resume_text, height=250)

        if st.button("Analyze with AI"):
            with st.spinner("Analyzing resume..."):
                prompt = f"Analyze the following resume:\n{resume_text}"
                ai_output = ask_ai(prompt)
                
                st.session_state['history'].append(ai_output) # Save to history
                st.subheader("AI Analysis Result")
                st.write(ai_output)
                st.success("Analysis Done!")

# ---------------------------------
# LOGIN/REGISTER UI
# ---------------------------------
if not st.session_state['logged_in']:
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")
        if st.button("Login"):
            if st.session_state['users'].get(user) == pwd:
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Invalid credentials!")
                
    with tab2:
        new_user = st.text_input("New Username")
        new_pwd = st.text_input("New Password", type="password")
        if st.button("Register"):
            st.session_state['users'][new_user] = new_pwd
            st.success("Registration successful! Please login.")
else:
    show_main_app()
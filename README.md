# 📄 AI Resume Analyzer (Groq + Llama 3)

An AI-powered Resume Analyzer built using Python, Streamlit, Groq API, and Llama 3. This application allows users to upload resumes in PDF, DOCX, or TXT format and receive instant AI-generated feedback and analysis.

---

## 🚀 Features

* 🔐 User Login & Registration System
* 📄 Resume Upload Support

  * PDF Files
  * DOCX Files
  * TXT Files
* 🤖 AI-Powered Resume Analysis using Groq + Llama 3
* 📋 Resume Content Extraction
* 📚 Analysis History Tracking
* 🎯 Instant Resume Evaluation
* 🌐 Interactive Streamlit Web Interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API
* Llama 3.3 70B Versatile
* PyPDF2
* python-docx

---

## 📂 Project Structure

```bash
Resume_Analysis/
│
├── resume.py
├── README.md
└── requirements.txt
```

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/Komal-Dhamange/Resume_Analysis.git
cd Resume_Analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit
pip install PyPDF2
pip install python-docx
pip install groq
```

---

## 🔑 Groq API Setup

Create a Groq API key from:

https://console.groq.com/keys

Replace the API key in `resume.py`:

```python
client = Groq(api_key="YOUR_API_KEY")
```

---

## ▶️ Run the Application

Open terminal in the project directory and run:

```bash
streamlit run resume.py
```

The application will automatically open in your browser.

---

## 📖 How It Works

1. Register a new account or login.
2. Upload a Resume (PDF/DOCX/TXT).
3. Resume text is extracted automatically.
4. Click **Analyze with AI**.
5. Groq Llama 3 model analyzes the resume.
6. View AI-generated feedback and suggestions.
7. Previous analyses are stored in session history.

---

## 🎯 Use Cases

* Students preparing resumes
* Freshers applying for internships
* Job seekers improving CV quality
* Career guidance and resume review
* Interview preparation

---

## 📸 Application Highlights

* Clean Streamlit Interface
* Secure Login System
* Multi-format Resume Support
* AI-Powered Resume Insights
* Analysis History Management

---

## 👩‍💻 Author

**Komal Dhamange**

GitHub: https://github.com/Komal-Dhamange

---

## ⭐ Future Enhancements

* Resume Score Generation
* ATS Compatibility Checker
* Skill Gap Analysis
* Resume Improvement Suggestions
* Download AI Analysis Report
* Resume vs Job Description Matching
* Multi-Language Resume Support

---

## 📜 License

This project is developed for educational and learning purposes.
Feel free to explore, modify, and enhance it.

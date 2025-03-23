import streamlit as st
from PyPDF2 import PdfReader
from pptx import Presentation   
import pandas as pd
import time
import datetime  # Import datetime for the current year
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🎨 **Set Page Configuration to Wide Mode and Add Custom Favicon**
st.set_page_config(
    layout="wide",
    page_title="AI Resume Ranking Analyzer",  # Set the page title
    page_icon="https://i.postimg.cc/hvGybMwQ/logo1.jpg"  # Custom favicon URL
)

# 🎨 **Custom CSS for a Light/Dark Toggle Button and Footer**
st.markdown("""
    <style>
    body { margin: 0; padding: 0; }
    .toggle-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }
    .toggle-switch {
        position: relative;
        display: inline-block;
        width: 60px;
        height: 34px;
    }
    .toggle-switch input {
        opacity: 0;
        width: 0;
        height: 0;
    }
    .slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #ccc;
        transition: 0.4s;
        border-radius: 34px;
    }
    .slider:before {
        position: absolute;
        content: "";
        height: 26px;
        width: 26px;
        left: 4px;
        bottom: 4px;
        background-color: white;
        transition: 0.4s;
        border-radius: 50%;
    }
    input:checked + .slider {
        background-color: #4CAF50;
    }
    input:checked + .slider:before {
        transform: translateX(26px);
    }

    /* Footer Styles */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: transparent;
        text-align: center;
        padding: 10px 0;
        font-size: 12px;
        color: gray;
        z-index: 1000;
    }

    /* Custom Title with Logo */
    .title-container {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .title-logo {
        width: 50px;
        height: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# 🕶️ **Toggle Light/Dark Mode**
dark_mode = st.checkbox("🌙 Dark Mode", value=True)

if dark_mode:
    st.markdown("""
        <style>
        body { background-color: #121212; color: white; }
        .stApp { background-color: #1E1E1E; }
        h1 { color: #4CAF50; }
        .footer { color: white; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body { background-color: white; color: black; }
        .stApp { background-color: #F0F0F0; }
        h1 { color: #000000; }
        .footer { color: gray; }
        </style>
    """, unsafe_allow_html=True)

# 📌 **Page Title with Custom Logo**
st.markdown(
    """
    <div class="title-container">
        <img src="https://i.postimg.cc/ncynhwCL/logo.png" class="title-logo">
        <h1>AI Resume Ranking Analyzer</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# 📝 **Job Description**
st.header("📝 Job Description")
job_description = st.text_area("Enter the job description...", height=150)

# 📤 **Upload Resumes**
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF and PPTX files", type=["pdf", "pptx"], accept_multiple_files=True)

# 📌 **Extract Text from PDF Resumes**
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = "".join([page.extract_text() or "" for page in pdf.pages])
    return text.strip()

# 📌 **Rank Resumes Using TF-IDF & Cosine Similarity**
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    job_desc_vector = vectors[0]
    resume_vectors = vectors[1:]
    return cosine_similarity([job_desc_vector], resume_vectors).flatten()

# 📌 **AI Suggestions for Resume Improvement**
def generate_resume_tips(score):
    if score > 80:
        return "🔥 Excellent match! Your resume is well-optimized."
    elif score > 60:
        return "✅ Good match! Consider adding more relevant keywords."
    else:
        return "⚡ Low match! Try improving your skills section and adding industry-specific terms."

# 📈 **Start Ranking Process**
if uploaded_files and job_description:
    st.header("📈 Resume Rankings")

    resumes = [extract_text_from_pdf(file) for file in uploaded_files]

    # Progress Bar
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)

    # Calculate Scores
    scores = rank_resumes(job_description, resumes)

    # Create Results DataFrame
    results_df = pd.DataFrame({
        "Resume": [file.name for file in uploaded_files],
        "Match Score (%)": (scores * 100).round(2),
        "AI Suggestion": [generate_resume_tips(score * 100) for score in scores]
    }).sort_values(by="Match Score (%)", ascending=False)

    # Display Results
    st.dataframe(results_df.style.format({"Match Score (%)": "{:.2f}"}), use_container_width=True)
    st.success(f"✅ Ranking Complete! 🎯 Top Match: **{results_df.iloc[0]['Resume']}**")

# 🦶 **Footer Section**
current_year = datetime.datetime.now().year  # Get the current year dynamically
st.markdown(
    f"""
    <div class="footer">
        Copyright ©{current_year} All rights reserved | Don't forget to give feedback ❤️<br>
        Made by <b>Arvind_67</b> & <b>NRZ Tech Solutions</b>
    </div>
    """,
    unsafe_allow_html=True  # Allow HTML to style the footer
)
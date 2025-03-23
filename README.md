# 🚀 AI Resume Ranking Analyzer
<img src="https://i.postimg.cc/ncynhwCL/logo.png" alt="App Logo" width="200">


### An AI tool that screens and ranks resumes automatically, based on job requirements.

## 📌 Overview
Welcome to the **AI Resume Ranking Analyzer**, a powerful tool designed to help recruiters and hiring managers efficiently rank resumes based on their relevance to a job description. This system uses **TF-IDF** and **Cosine Similarity** to analyze and rank resumes, also use **Natural Language Processing (NLP)** and **Machine Learning (ML)** providing AI-driven suggestions for improvement.

---

## 🌟 Features
- 📂 **Upload multiple resumes** (PDF format, max 200MB per file)
- 📝 **Input job description** to match candidate profiles
- 📊 **Resume ranking system** using NLP and ML techniques
- 🔍 **Match score (%)** to evaluate candidate relevance
- 💡 **AI suggestions** for resume improvement
- 🎨 **Light/Dark Mode**: Toggle between light and dark themes for a comfortable viewing experience.
- 🖥️✨ - **User-Friendly Interface**: Simple and intuitive design for easy navigation.
- 📊 **Progress Bar**: Visual feedback during the ranking process.
- ☁ **Deployed using Streamlit**

## 🛠️ Technologies Used

- **Frontend & UI**: 
  - **Streamlit**: For building the web app interface.

- **NLP Processing**: 
  - **spaCy**: For advanced natural language processing tasks.
  - **NLTK**: For text preprocessing and tokenization.
  - **TF-IDF**: For term frequency-inverse document frequency calculations.

- **Machine Learning**: 
  - **Scikit-learn**: For machine learning algorithms and utilities.
  - **Vectorizer**: For converting text data into numerical features.
  - **Cosine Similarity**: For measuring the similarity between resumes and job descriptions.

- **Data Handling**: 
  - **Pandas**: For data manipulation and displaying results.
  - **NumPy**: For numerical computations and array handling.

- **Deployment**: 
  - **Streamlit Cloud**: For deploying the app to the cloud.
  - **Local Hosting**: For running the app locally.

---

## 📷 Screenshots
### Upload Resumes & Enter Job Description
<p align="center">
  <img src="https://i.postimg.cc/zvR8Zm8r/Screenshot-2025-03-22-235312.png" alt="Upload Resume 1" width="100%" />
</p>

<p align="center">
  <img src="https://i.postimg.cc/dQXrFqsb/Screenshot-2025-03-22-233803.png" alt="Upload Resume 2" width="100%" />
</p>

### Resume Ranking Results

<p align="center">
  <img src="https://i.postimg.cc/bvzFL821/Screenshot-2025-03-23-002435.png" alt="Resume Ranking Results" width="100%" />
</p>

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit
- PyPDF2
- Pandas
- Scikit-learn

---

## 🏗️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/67arvind/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
      OR
python -m streamlit run app.py
```

4. Open your browser and navigate to http://localhost:8501

---
5. ### **Live Demo:** 
---
[![live_app](https://img.shields.io/badge/live_app-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://resumeanalyzerwithai.streamlit.app/)
---

## 🎯 How It Works
1. **Upload resumes:** Upload multiple resumes in PDF/PPTX format
2. **Enter job description :** Provide the job description in the text area.
3. **Rank Resumes:** The system calculates the similarity between the job description and each resume using **TF-IDF** and **Cosine Similarity**.
4. **View Results:** See the ranked resumes along with their match scores and AI suggestions.
5. 🎯 **Top Match:** Show one Top Resume.

## 📌 Future Enhancements
- ✅ Support for DOCX and other file formats
- ✅ Advanced AI-based skill extraction
- ✅ Cloud-based deployment

## 💡 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

### **Need Help?**
---
 - If you're new to open-source contributions or need help, feel free to connect with us on [LinkedIn](https://www.linkedin.com/in/arvind-kumar-424554196/) open an issue, or reach out to us. We're happy to guide you!

---
Thank you for contributing! 🚀
---
## **License**

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)License. See the LICENSE file for details.

## 🔗 Connect With Me

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arvind-kumar-424554196/)



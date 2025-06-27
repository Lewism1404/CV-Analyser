# CV Analyser – AI-Powered Resume Reviewer

This web application will be used to analyse a CV and give feedback, The reason for this is that most companies that hire have an AI look through the CVs and reject/accept them based on some criteria. Knowing if your CV is good could improve the likelihood of your applications having more success and reaching further stages.

---

## What It Does

-  Parses resumes (PDF and DOCX)
-  Extracts content like skills, experience, education
-  Uses NLP to analyze relevance to job descriptions
-  Returns a structured report and optimization suggestions
-  Ready to connect with a frontend for real-time feedback

---

## Tech Stack

- **Backend**: Python 3.10, FastAPI
- **Parsing**: PyMuPDF, python-docx
- **NLP**: spaCy, transformers, scikit-learn
- **Environment**: Conda
- **Frontend**: React

---

## Getting Started

> These steps require you to use **Anaconda**

### 1. Clone the repository

git clone https://github.com/your-username/CV-Analyser.git
cd CV-Analyser

### 2. Create the Conda Enviroment

conda create -n cv-analyser python=3.10
conda activate cv-analyser

### 3. Install Packages

pip install -r requirements.txt
python -m spacy downnload en_core_web_sm

### 4. Run the FastAPI server

uvicorn app.main:app --reload

### Test the API

Once the server is running, open your browser and go to:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- Click on the `/upload` endpoint
- Click **"Try it out"**
- Upload a `.pdf` or `.docx` resume
- Click **Execute**
- You should see the extracted text in the response!

 

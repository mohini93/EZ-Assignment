# EZ-Assignment
# 🧠 EZ-Assignment  
## 📘 Smart Assistant for Research Summarization

> An AI-powered assistant that reads uploaded documents (PDF/TXT), understands their content, and performs tasks like summarization, contextual question answering, and logic-based reasoning.

---

## 🚀 Features

### 📂 Document Upload
- Supports both `.pdf` and `.txt` formats
- Suitable for structured documents: research papers, reports, manuals

### 📝 Auto Summary
- Generates a concise summary (up to **150 words**) automatically upon upload

### 🔄 Two Interaction Modes

#### 1. **Ask Anything**
- Ask any free-form question based on the uploaded document
- The assistant answers with relevant content **with justification snippets**

#### 2. **Challenge Me**
- Generates **3 comprehension/logic-based questions**
- User answers → Assistant evaluates → Feedback with explanation

### 📖 Contextual Answering
- All answers are grounded in the uploaded document
- ❌ No hallucinated or made-up responses
- ✅ Justifications are included using source text excerpts

---

## 🧱 Architecture

- **Frontend**: `Streamlit`
- **Backend**: 🤗 Hugging Face Transformers

### 🔧 Components
- **Document Upload**: `fitz (PyMuPDF)` for PDFs, raw reading for TXTs
- **Summarization**: `DistilBART`
- **Qhttps://translate.google.com/uestion Answering**: `DistilBERT`
- **Sentence Embedding**: `MiniLM`

---

## 📁 File Structure

project/
├── requirements.txt # Python dependencies
├──  train.py # Model loading (summarizer, QnA, embedder)
├──  train.py # Model loading (summarizer, QnA, embedder)
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 🔁 Step 1: Clone the Repository
```bash
git clone https://github.com/mohini93/ez.git
cd ez
##🧪 Step 2: Create & Activate Virtual Environment
bash
Copy
Edit
# 👉 Windows
python -m venv .venv
.venv\Scripts\activate

# 👉 macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
##📦 Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
⚠️ If fitz (PyMuPDF) causes issues, install it separately:

bash
Copy
Edit
pip install PyMuPDF
🚀 Step 4: Launch the App
bash
Copy
Edit
streamlit run streamlit_app.py
Once launched, the app will automatically open in your browser at:
🔗 http://localhost:8501
Evaluation Criteria Mapping

Evaluation Area                          Status  
Response Quality & Justification       ✅ Yes  
Reasoning Mode Functionality           ✅ Yes  
UI/UX and Smooth User Flow            ✅ Yes  
Code Structure and Documentation      ✅ Yes  
Creativity and Bonus Features          🟡 Partial  
Minimal Hallucination & Context Use    ✅ Yes
📊 Evaluation Criteria Mapping
Evaluation Area	Implemented
Response Quality & Justification	✅ Yes
Reasoning Mode Functionality	✅ Yes
UI/UX and Smooth User Flow	✅ Yes
Code Structure and Documentation	✅ Yes
Creativity and Bonus Features	🟡 Partial
Minimal Hallucination & Context Use	✅ Yes

🔥 Bonus Features (Partially Implemented)
📌 Document snippet justifications

🧠 Memory-based follow-up and answer highlighting (planned)


📜 License
This project is developed for educational and evaluation purposes as part of the EZ Assignment.
© 2025 Mohini Pal



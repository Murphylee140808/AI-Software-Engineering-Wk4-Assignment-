# 🤖 AI in Software Engineering — Week 4 Assignment

**Author:** Omowumi Akindehinde

**Program:** Power Learn Project (PLP) — July Cohort

**Project Title:** AI in Software Development: Theory, Practice & Ethics

---

## 📘 Project Overview

This repository contains all deliverables for the **AI in Software Engineering (Week 4 Assignment)** under the  **Power Learn Project (PLP)** .

It demonstrates how AI tools enhance software development efficiency — from **AI-assisted code generation and automated testing** to  **ethical model deployment and innovation proposals** .

---

## 🧩 Repository Structure

AI-Software-Engineering-Wk4-Assignment-/
├── README.md
├── requirements.txt
├── sort_dicts_AI.py
├── sort_dicts_Manual.py
├── breast-cancer-diagonose.ipynb
├── breast-cancer-diagonose.pkl
├── AI_Login_Test_Script/
│   └── AI_Login_Test.side
├── Screenshot_login_test_results/
├── reports/
│   ├── AI-in-Software-Development-Theory-Practice-and-Ethics.pdf
│   ├── DocuMind_AI_Tool_Proposal_Omowumi_Akindehinde.pdf
├── presentation/
│   └── ai_demo_video.mp4


## ⚙️ Run Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/`Murphylee140808`/AI-Software-Engineering-Wk4-Assignment-.git
cd AI-Software-Engineering-Wk4-Assignment-

2️⃣ Create and Activate Virtual Environment (Recommended)

python -m venv venv

# Activate it:

# On Windows:

venv\Scripts\activate

# On macOS/Linux:

source venv/bin/activate

### 3️⃣ Install Dependencies

Install all required libraries:

pip install -r requirements.txt


### 4️⃣ Run the Notebook

Launch Jupyter Notebook and execute all cells in:

jupyter notebook breast-cancer-diagonose.ipynb

* The notebook will  **load images, preprocess data, train a Random Forest model** , and display evaluation metrics (Accuracy & F1-score).
* A serialized model is saved as:

  breast-cancer-diagonose.pkl

### 5️⃣ Run Python Scripts

Test AI-assisted vs manual code sorting:

python sort_dicts_Manual.py
python sort_dicts_AI.py


### 6️⃣ View Automated Test Script

To replay the Selenium-based AI login test:

1. Open `AI_Login_Test_Script/AI_Login_Test.side` in  **Selenium IDE** .
2. Click  **Run All Tests** .
3. View results in `Screenshot_login_test_results/`.

### 7️⃣ Explore Reports & Presentation

* 📄 **Reports:**

  * `reports/AI-in-Software-Development-Theory-Practice-and-Ethics.pdf`
  * `reports/DocuMind_AI_Tool_Proposal_Omowumi_Akindehinde.pdf`
* 🎥 **Demo Video:**

  * `presentation/ai_demo_video.mp4`

  ## 🧠 Key Components

  ### 🔹 Part 1: Theoretical Analysis

  * Short-answer explanations on  **AI code generation** ,  **supervised vs unsupervised learning** , and  **bias in AI personalization** .
  * Case study showing how **AIOps** improves deployment (e.g., Harness, CircleCI).

  ### 🔹 Part 2: Practical Implementation

  * **AI-powered code sorting** comparison (Manual vs Copilot-assisted).
  * **Automated testing** with Selenium IDE enhanced by AI element recognition.
  * **AI model training** using TensorFlow and RandomForestClassifier for breast cancer classification.

  ### 🔹 Part 3: Ethical Reflection

  * Discusses dataset bias and fairness issues in predictive AI models.
  * Explores how **IBM AI Fairness 360** helps detect and mitigate bias.

  ### 🔹 Bonus Task: Innovation Challenge

  * Proposal: **DocuMind AI** — an intelligent documentation generator that summarizes code and generates professional developer docs using NLP.

  ---

  ## 📊 Model Performance

  | Metric   | Score |
  | -------- | ----- |
  | Accuracy | ~0.92 |
  | F1-Score | ~0.91 |

  *(Exact values may vary depending on training splits.)*

  ---

  ## 📚 Tools & Technologies

  * **Languages:** Python
  * **Libraries:** TensorFlow, scikit-learn, pandas, numpy, matplotlib, joblib
  * **Testing:** Selenium IDE
  * **Reporting:** Jupyter Notebook, ReportLab (for PDFs)
  * **AI Assistant:** GitHub Copilot

  ---

  ## ✨ Author

  **Omowumi Maruff Akindehinde (Techgod)**

  💻 Data Scientist | Frontend Developer | Notion Expert

  📫 [LinkedIn](#) | [GitHub]()

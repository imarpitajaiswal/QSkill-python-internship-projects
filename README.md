# 🚀 QSkill Python Internship Projects

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Flask-REST%20API-000000?style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/badge/Google-Gemini%202.5-4285F4?style=for-the-badge&logo=google"/>
  <img src="https://img.shields.io/badge/NLP-TextBlob-blue?style=for-the-badge"/>
</p>

## 📌 Overview

This repository contains three practical Python projects developed during my **1-Month Python Internship at QSkill**.

Each project focuses on a different area of Artificial Intelligence, Machine Learning, and Backend Development.

The repository demonstrates hands-on implementation of:

- AI Agent Development
- Machine Learning Model Training
- REST API Development
- Natural Language Processing
- Environment Variable Management
- Model Serialization

---

# 📂 Repository Structure

```
QSKILL
│
├── agent_engine
│   └── enterprise_agent.py
│
├── regression_engine
│   ├── train.py
│   ├── predict.py
│   ├── housing_data.csv
│   └── valuation_model.pkl
│
├── sentiment_api
│   └── app.py
│
└── .gitignore
```

---

# 🤖 Project 1 — AI Enterprise Agent

An intelligent conversational assistant powered by **Google Gemini** with integrated real-time web search.

### Features

- Google Gemini 2.5 Flash
- Stateful chat session
- DuckDuckGo real-time search
- Automatic function calling
- Environment variable security
- Session memory
- Professional prompt engineering

### Technologies

- Google Gemini SDK
- DuckDuckGo Search
- Python
- python-dotenv

---

# 📈 Project 2 — House Price Prediction

A machine learning regression project that predicts property prices based on property characteristics.

### Features

- Synthetic dataset generation
- Linear Regression model
- Model serialization using Pickle
- Train/Test split
- RMSE evaluation
- R² Score evaluation
- Real-time prediction script

### Input Features

| Feature | Description |
|----------|-------------|
| Rooms | Number of rooms |
| Size | Area in square feet |
| Location Grade | Property location rating |

### Output

Estimated Property Price (Lakhs INR)

---

# 💬 Project 3 — Sentiment Analysis REST API

A Flask-based REST API that analyzes text sentiment using TextBlob.

### Features

- RESTful API
- JSON request validation
- Text polarity analysis
- Subjectivity analysis
- Positive / Neutral / Negative classification
- Standardized JSON responses
- Error handling

Example Endpoint

```
POST /api/v1/sentiment
```

Example Request

```json
{
    "text":"This internship was amazing!"
}
```

Example Response

```json
{
  "status":"success",
  "data":{
      "classification":"Positive",
      "metrics":{
          "polarity_score":0.75,
          "subjectivity_score":0.6
      }
  }
}
```

---

# 🛠 Tech Stack

- Python
- Google Gemini API
- Flask
- TextBlob
- Scikit-learn
- Pandas
- NumPy
- DuckDuckGo Search
- Pickle
- dotenv

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/imarpitajaiswal/QSKILL.git

cd QSKILL
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶ Running the Projects

### AI Agent

```bash
python agent_engine/enterprise_agent.py
```

### Train Regression Model

```bash
python regression_engine/train.py
```

### Predict Property Price

```bash
python regression_engine/predict.py
```

### Start Sentiment API

```bash
python sentiment_api/app.py
```

---

# 📚 Learning Outcomes

During this internship, I gained practical experience in:

- Python Programming
- AI Agent Development
- REST API Design
- Machine Learning
- Data Preprocessing
- Model Evaluation
- Environment Variable Security
- Natural Language Processing
- Version Control using Git & GitHub

---

# 🚀 Future Improvements

- Docker Support
- FastAPI Migration
- Model Deployment
- Streamlit Dashboard
- Authentication
- Database Integration
- CI/CD Pipeline
- Unit Testing

---

# 👩‍💻 Author

**Arpita Jaiswal**

MCA (Artificial Intelligence & Machine Learning)

GitHub:
https://github.com/imarpitajaiswal

LinkedIn:
https://linkedin.com/in/imarpitajaiswal

---

⭐ If you found this repository useful, consider giving it a star.

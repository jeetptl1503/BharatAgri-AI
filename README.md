# BharatAgri AI — Intelligent Crop & Yield Advisory System

🌾 An AI-powered agricultural decision-support platform for Indian farmers with region-specific crop recommendations, yield forecasting, risk analysis, multilingual support, and an AI chatbot.

## Quick Start

### Prerequisites
- Python 3.10+

### Setup & Run

```bash
# 1. Navigate to backend
cd backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train ML models (first time only)
python -m app.ml.train_models

# 4. Start the server
python -m uvicorn app.main:app --reload --port 8000
```

Open **http://localhost:8000** in your browser.

## Features

| Feature | Description |
|---------|-------------|
| 🌾 Smart Crop Recommendation | AI suggests top 3 crops for your soil, climate, and region |
| 📊 Yield Prediction | Predict expected output with state-level accuracy |
| ⚡ Risk Analysis | Climate deviation, soil gap, and seasonal risk scoring |
| 🌐 Multilingual | English, Hindi, Punjabi, Marathi, Telugu, Tamil, Bengali |
| 🤖 AI Chatbot | Agriculture-focused assistant (NPK, soil, schemes) |
| 📈 Analytics | Prediction history, yield comparison charts |
| 🌡️ Climate Simulation | Simulate rainfall/temperature changes |
| 🔒 JWT Authentication | Secure user accounts |

## Architecture

```
backend/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── config.py             # Settings
│   ├── models/database.py    # SQLAlchemy models
│   ├── routes/
│   │   ├── auth.py           # JWT auth
│   │   ├── predict.py        # Crop/yield/risk APIs
│   │   ├── chatbot.py        # AI chatbot
│   │   └── reference.py      # State/district/soil data
│   ├── ml/
│   │   ├── train_models.py   # Model training pipeline
│   │   └── predictor.py      # Prediction engine
│   └── data/
│       ├── india_data.py     # 16 states, 25 crops reference
│       └── generate_datasets.py
├── trained_models/           # Serialized ML models
├── frontend/                 # HTML/CSS/JS SPA
│   ├── index.html
│   ├── css/styles.css
│   └── js/ (i18n, api, auth, pages, app)
└── requirements.txt
```

## API Documentation

Visit **http://localhost:8000/docs** for interactive Swagger documentation.

## Coverage

- **16 Indian states** with district-level data
- **25 crops** with optimal growing conditions
- **3 ML models** (RandomForest, GradientBoosting, Rule-based Risk)
- **7 languages** for multilingual UI

## Tech Stack

- **Backend:** FastAPI, scikit-learn, SQLAlchemy, SQLite
- **Frontend:** Vanilla HTML/CSS/JS SPA
- **ML:** RandomForestClassifier, GradientBoostingRegressor
- **Auth:** JWT + bcrypt
# BharatAgri-AI

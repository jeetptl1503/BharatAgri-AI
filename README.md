# 🌾 BharatAgri AI — Intelligent Crop & Yield Advisory System

<div align="center">

**AI-powered agricultural decision-support platform for Indian farmers**

[🌐 Live Demo] (https://bharatagri-ai.vercel.app/)· [📖 API Docs](https://bharat-agri-ai.vercel.app/api/docs) · [🐛 Report Bug](https://github.com/jeetptl1503/BharatAgri-AI/issues)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?style=flat-square&logo=fastapi&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployed_on-Vercel-000?style=flat-square&logo=vercel&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## 🎯 What is BharatAgri AI?

BharatAgri AI is a full-stack intelligent advisory system that helps Indian farmers make data-driven decisions. It provides **crop recommendations**, **yield predictions**, and **risk analysis** based on soil nutrients, climate data, and regional conditions — covering **16 states**, **25+ crops**, and **8 Indian languages**.

> 🟢 **Try it live**: https://bharatagri-ai.vercel.app/

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌱 **Smart Crop Recommendation** | Scores 25+ crops against your soil (NPK, pH), climate (temp, rainfall, humidity), soil type, season, and state — returns top 3 with explanations |
| 📊 **Yield Prediction** | Estimates expected output in tons/hectare using crop condition matching, state averages, and season fit |
| ⚠️ **Risk Analysis** | Hybrid scoring system flags temperature, rainfall, pH, soil, season, and NPK risks with detailed factors |
| 🤖 **AI Chatbot** | Ask about any crop, state, NPK, soil health cards, government schemes (PM-KISAN, KCC, etc.) |
| 🌐 **8 Languages** | English, हिन्दी, ਪੰਜਾਬੀ, मराठी, తెలుగు, தமிழ், বাংলা, ગુજરાતી — with proper Indic fonts (Noto Sans) |
| 🗺️ **16 States** | District-level soil types, climate ranges, and major crop data |
| 🔐 **JWT Authentication** | Secure signup/login with bcrypt password hashing |
| 📈 **Prediction History** | Dashboard tracks all your past predictions |

---

## 🖥️ Screenshots

| Home Page | Advisory Form | Chatbot |
|-----------|--------------|---------|
| Landing with hero, features, and stats | Guided form with auto-filled climate | Interactive agriculture assistant |

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI · SQLAlchemy · SQLite |
| **Frontend** | Vanilla HTML/CSS/JS (SPA) |
| **Auth** | JWT (python-jose) · bcrypt |
| **Predictions** | Rule-based engine using agronomic crop condition data |
| **Chatbot** | Knowledge-base system with multilingual responses |
| **Fonts** | Google Fonts — Inter, Poppins, Noto Sans (Devanagari, Gujarati, Gurmukhi, Telugu, Tamil, Bengali) |
| **Deployment** | Vercel (Python serverless + static frontend) |

---

## 📁 Project Structure

```
AIdeaForge/
├── api/index.py                  # Vercel serverless entry point
├── vercel.json                   # Vercel routing config
├── requirements.txt              # Python dependencies
├── frontend/                     # Static frontend (served by Vercel)
│   ├── index.html                # Main SPA shell
│   ├── css/styles.css            # Full design system + Indic font support
│   └── js/
│       ├── i18n.js               # 8-language translation system
│       ├── api.js                # API client with JWT auth
│       ├── auth.js               # Login/register/logout logic
│       ├── pages.js              # All SPA page renderers
│       └── app.js                # Router and navigation
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI app (API-only on Vercel, full locally)
│   │   ├── config.py             # Settings (auto-detects Vercel environment)
│   │   ├── routes/
│   │   │   ├── auth.py           # Register, login, profile (JWT + bcrypt)
│   │   │   ├── predict.py        # Crop, yield, risk, full prediction
│   │   │   ├── chatbot.py        # Multilingual chatbot (6 topics, 3 languages)
│   │   │   └── reference.py      # States, districts, soil types, climate
│   │   ├── ml/
│   │   │   └── predictor.py      # Rule-based prediction engine
│   │   ├── models/
│   │   │   └── database.py       # SQLAlchemy models (User, PredictionHistory, ChatHistory)
│   │   └── data/
│   │       └── india_data.py     # 16 states, 25 crops, soil & climate reference data
│   └── trained_models/           # ML models (for local dev, not used on Vercel)
└── README.md
```

---

## 🚀 Quick Start

### Option 1: Use the Live Demo
👉 **[https://bharat-agri-ai.vercel.app](https://bharat-agri-ai.vercel.app)**

1. Click **Sign Up** → create an account
2. Go to **Advisory** → select state, district, enter soil data
3. Click **Analyze** → get crop recommendations, yield forecast, and risk report
4. Try the **Chatbot** → ask "What is NPK?" or "Tell me about Rice"
5. Switch language from the dropdown — the entire UI translates

### Option 2: Run Locally

```bash
# Clone the repo
git clone https://github.com/jeetptl1503/BharatAgri-AI.git
cd BharatAgri-AI

# Create virtual environment
cd backend
python -m venv ../.venv
..\.venv\Scripts\activate         # Windows
# source ../.venv/bin/activate    # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the server
python -m uvicorn app.main:app --reload --port 8000
```

Open **http://localhost:8000**

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/register` | Register a new user |
| `POST` | `/api/auth/login` | Login and get JWT token |
| `GET` | `/api/auth/me` | Get current user profile |
| `POST` | `/api/predict/full` | Full prediction (crop + yield + risk) |
| `POST` | `/api/predict/crop` | Crop recommendation only |
| `POST` | `/api/predict/yield` | Yield prediction only |
| `POST` | `/api/predict/risk` | Risk analysis only |
| `GET` | `/api/predict/history` | User's prediction history |
| `POST` | `/api/chatbot/message` | Chat with AI assistant |
| `GET` | `/api/reference/states` | List all supported states |
| `GET` | `/api/reference/districts/{state}` | Districts for a state |
| `GET` | `/api/reference/climate/{state}` | Climate data for a state |
| `GET` | `/health` | Health check |

> 📖 Full interactive docs: [/api/docs](https://bharat-agri-ai.vercel.app/api/docs) (Swagger UI)

---

## 🌍 Supported Languages

| Code | Language | Script |
|------|----------|--------|
| `en` | English | Latin |
| `hi` | हिन्दी (Hindi) | Devanagari |
| `pa` | ਪੰਜਾਬੀ (Punjabi) | Gurmukhi |
| `mr` | मराठी (Marathi) | Devanagari |
| `te` | తెలుగు (Telugu) | Telugu |
| `ta` | தமிழ் (Tamil) | Tamil |
| `bn` | বাংলা (Bengali) | Bengali |
| `gu` | ગુજરાતી (Gujarati) | Gujarati |

Each language uses its dedicated **Noto Sans** font variant for proper script rendering.

---

## 🗺️ Supported States & Crops

**16 States:** Andhra Pradesh, Assam, Bihar, Gujarat, Haryana, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Odisha, Punjab, Rajasthan, Tamil Nadu, Telangana, Uttar Pradesh, West Bengal

**25+ Crops:** Rice, Wheat, Maize, Sugarcane, Cotton, Groundnut, Soybean, Mustard, Gram, Bajra, Jowar, Barley, Lentil, Potato, Onion, Tomato, Chilli, Turmeric, Ginger, Banana, Mango, Coconut, Tea, Coffee, Jute

---

## 📜 License

MIT — free to use, modify, and distribute.

---

<div align="center">

**Built with ❤️ for Indian Farmers**

🌾 *Empowering agriculture with AI* 🌾

</div>

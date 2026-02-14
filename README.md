# 🌾 BharatAgri AI — Intelligent Crop & Yield Advisory System

> AI-powered agricultural decision-support platform for Indian farmers.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌱 **Smart Crop Advisory** | AI recommends top 3 crops for your soil + climate |
| 📊 **Yield Prediction** | ML model forecasts expected output (R²=0.95) |
| ⚠️ **Risk Analysis** | Hybrid rule+ML risk scoring with factors |
| 🤖 **AI Chatbot** | Ask about NPK, soil, schemes, any crop or state |
| 🌐 **8 Languages** | EN, हिन्दी, ਪੰਜਾਬੀ, मराठी, తెలుగు, தமிழ், বাংলা, ગુજરાતી |
| 🗺️ **16 States** | District-level soil & climate data |

## 🛠 Tech Stack

- **Backend:** FastAPI + SQLAlchemy + SQLite
- **ML:** scikit-learn (RandomForest, GradientBoosting)
- **Frontend:** Vanilla HTML/CSS/JS SPA
- **Auth:** JWT + bcrypt
- **Deploy:** Vercel (serverless Python + static)

---

## 🚀 Deploy to Vercel

### Prerequisites
- [Vercel CLI](https://vercel.com/docs/cli) installed: `npm i -g vercel`
- A Vercel account (free tier works)

### Steps

```bash
# 1. Navigate to project root
cd AIdeaForge

# 2. Login to Vercel
vercel login

# 3. Deploy
vercel --prod
```

That's it! Vercel will:
- Install Python dependencies from `requirements.txt`
- Deploy `api/index.py` as a serverless function
- Serve `frontend/` as static files
- Give you a **public URL** like `https://bharatagri-ai.vercel.app`

---

## 💻 Local Development

```bash
# 1. Create virtual environment
cd backend
python -m venv ../.venv
..\.venv\Scripts\activate       # Windows
# source ../.venv/bin/activate   # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train ML models (first time only)
python -m app.ml.train_models

# 4. Run the server
python -m uvicorn app.main:app --reload --port 8000
```

Open **http://localhost:8000** in your browser.

---

## 📁 Project Structure

```
AIdeaForge/
├── api/index.py              # Vercel serverless entry point
├── vercel.json               # Vercel routing config
├── requirements.txt          # Python deps (root for Vercel)
├── frontend/                 # Static frontend (served by Vercel)
│   ├── index.html
│   ├── css/styles.css
│   └── js/ (i18n, api, auth, pages, app)
├── backend/
│   ├── app/
│   │   ├── main.py           # FastAPI app
│   │   ├── config.py         # Settings (auto-detects Vercel)
│   │   ├── routes/           # auth, predict, chatbot, reference
│   │   ├── ml/               # train_models.py, predictor.py
│   │   ├── models/           # SQLAlchemy models
│   │   └── data/             # india_data.py, CSV datasets
│   ├── trained_models/       # Serialized ML models
│   └── frontend/             # Local copy (served by FastAPI)
└── README.md
```

## 📜 License
MIT
# BharatAgri-AI

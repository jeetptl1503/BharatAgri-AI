"""
ML Predictor module for BharatAgri AI.
Loads trained models and runs predictions with explainability.
"""
import os
import numpy as np
import joblib
from app.data.india_data import CROP_CONDITIONS, CROP_AVG_YIELDS, STATES_DATA, SOIL_CHARACTERISTICS

MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "trained_models")

# Cached models
_models = {}


def _load_model(name):
    if name not in _models:
        path = os.path.join(MODEL_DIR, f"{name}.joblib")
        if os.path.exists(path):
            _models[name] = joblib.load(path)
        else:
            raise FileNotFoundError(f"Model {name} not found at {path}. Run train_models.py first.")
    return _models[name]


def predict_crop(n, p, k, temperature, humidity, ph, rainfall, soil_type, state, season):
    """
    Predict top 3 recommended crops with probabilities and explanations.
    """
    model = _load_model("crop_model")
    soil_enc = _load_model("soil_encoder")
    state_enc = _load_model("state_encoder")
    season_enc = _load_model("season_encoder")
    crop_enc = _load_model("crop_encoder")
    feature_names = _load_model("feature_names")

    # Handle unknown labels
    try:
        soil_encoded = soil_enc.transform([soil_type])[0]
    except ValueError:
        soil_encoded = 0
    try:
        state_encoded = state_enc.transform([state])[0]
    except ValueError:
        state_encoded = 0
    try:
        season_encoded = season_enc.transform([season])[0]
    except ValueError:
        season_encoded = 0

    features = np.array([[n, p, k, temperature, humidity, ph, rainfall,
                           soil_encoded, state_encoded, season_encoded]])

    # Get probabilities for all crops
    probabilities = model.predict_proba(features)[0]
    top_indices = np.argsort(probabilities)[::-1][:3]

    results = []
    for idx in top_indices:
        crop_name = crop_enc.inverse_transform([idx])[0]
        prob = probabilities[idx]
        explanation = _generate_crop_explanation(
            crop_name, n, p, k, temperature, humidity, ph, rainfall,
            soil_type, state, season, model.feature_importances_, feature_names
        )
        results.append({
            "crop": crop_name,
            "probability": round(float(prob) * 100, 1),
            "explanation": explanation
        })

    # Feature importance
    importance_dict = {}
    for fname, importance in zip(feature_names, model.feature_importances_):
        importance_dict[fname] = round(float(importance) * 100, 1)

    return {
        "recommendations": results,
        "feature_importance": importance_dict
    }


def _generate_crop_explanation(crop, n, p, k, temp, humidity, ph, rainfall,
                                soil_type, state, season, importances, feature_names):
    """Generate human-readable explanation for crop recommendation."""
    conditions = CROP_CONDITIONS.get(crop, {})
    reasons = []

    # Check which conditions match well
    if conditions:
        if conditions.get("temp") and conditions["temp"][0] <= temp <= conditions["temp"][1]:
            reasons.append(f"temperature ({temp:.0f}°C) falls within optimal range")
        if conditions.get("rainfall") and conditions["rainfall"][0] <= rainfall <= conditions["rainfall"][1]:
            reasons.append(f"rainfall ({rainfall:.0f}mm) matches ideal conditions")
        if conditions.get("ph") and conditions["ph"][0] <= ph <= conditions["ph"][1]:
            reasons.append(f"soil pH ({ph:.1f}) is suitable")
        if conditions.get("soil") and soil_type in conditions["soil"]:
            reasons.append(f"{soil_type} soil is well-suited")
        if conditions.get("season") and season in conditions["season"]:
            reasons.append(f"{season} season is ideal for cultivation")

        # NPK analysis
        n_range = conditions.get("n", (0, 999))
        if n_range[0] <= n <= n_range[1]:
            reasons.append(f"nitrogen level ({n:.0f}) is optimal")

    if not reasons:
        reasons.append("overall soil and climate conditions are compatible")

    state_info = STATES_DATA.get(state, {})
    major = state_info.get("major_crops", [])
    if crop in major:
        reasons.append(f"it is a major crop grown in {state}")

    explanation = f"{crop} is recommended because " + ", ".join(reasons[:4]) + "."
    return explanation


def predict_yield(state, district, crop, season, area, rainfall, temperature):
    """Predict crop yield for given conditions."""
    model = _load_model("yield_model")
    state_enc = _load_model("yield_state_encoder")
    crop_enc = _load_model("yield_crop_encoder")
    season_enc = _load_model("yield_season_encoder")
    district_enc = _load_model("yield_district_encoder")

    try:
        state_encoded = state_enc.transform([state])[0]
    except ValueError:
        state_encoded = 0
    try:
        crop_encoded = crop_enc.transform([crop])[0]
    except ValueError:
        crop_encoded = 0
    try:
        season_encoded = season_enc.transform([season])[0]
    except ValueError:
        season_encoded = 0
    try:
        district_encoded = district_enc.transform([district])[0]
    except ValueError:
        district_encoded = 0

    features = np.array([[state_encoded, district_encoded, crop_encoded,
                           season_encoded, area, rainfall, temperature]])

    predicted_yield = model.predict(features)[0]
    predicted_yield = max(0.1, predicted_yield)

    state_avg = CROP_AVG_YIELDS.get(crop, 2.0)
    total_production = predicted_yield * area
    yield_diff_percent = ((predicted_yield - state_avg) / state_avg) * 100

    return {
        "predicted_yield": round(float(predicted_yield), 2),
        "total_production": round(float(total_production), 2),
        "state_average_yield": round(float(state_avg), 2),
        "yield_difference_percent": round(float(yield_diff_percent), 1),
        "unit": "tons/hectare"
    }


def calculate_risk(n, p, k, ph, temperature, humidity, rainfall, soil_type, state, season, crop):
    """
    Calculate risk score using rule + ML hybrid approach.
    Returns risk level (Low/Moderate/High) with explanation.
    """
    risk_score = 0
    risk_factors = []

    conditions = CROP_CONDITIONS.get(crop, {})
    if not conditions:
        return {"risk_level": "Moderate", "risk_score": 50, "factors": ["Limited data for this crop"]}

    # Temperature risk
    temp_range = conditions.get("temp", (15, 35))
    if temperature < temp_range[0] - 5 or temperature > temp_range[1] + 5:
        risk_score += 25
        risk_factors.append(f"Temperature ({temperature:.0f}°C) significantly outside optimal range ({temp_range[0]}-{temp_range[1]}°C)")
    elif temperature < temp_range[0] or temperature > temp_range[1]:
        risk_score += 12
        risk_factors.append(f"Temperature ({temperature:.0f}°C) slightly outside optimal range")

    # Rainfall risk
    rain_range = conditions.get("rainfall", (500, 1500))
    if rainfall < rain_range[0] * 0.5 or rainfall > rain_range[1] * 1.5:
        risk_score += 25
        risk_factors.append(f"Rainfall ({rainfall:.0f}mm) far from ideal range ({rain_range[0]}-{rain_range[1]}mm)")
    elif rainfall < rain_range[0] or rainfall > rain_range[1]:
        risk_score += 12
        risk_factors.append(f"Rainfall ({rainfall:.0f}mm) outside optimal range")

    # pH risk
    ph_range = conditions.get("ph", (5.5, 7.5))
    if ph < ph_range[0] - 1 or ph > ph_range[1] + 1:
        risk_score += 20
        risk_factors.append(f"Soil pH ({ph:.1f}) significantly outside optimal range ({ph_range[0]}-{ph_range[1]})")
    elif ph < ph_range[0] or ph > ph_range[1]:
        risk_score += 10
        risk_factors.append(f"Soil pH ({ph:.1f}) slightly outside optimal range")

    # Soil type compatibility
    suitable_soils = conditions.get("soil", [])
    if suitable_soils and soil_type not in suitable_soils:
        risk_score += 15
        risk_factors.append(f"{soil_type} soil is not ideal for {crop} (preferred: {', '.join(suitable_soils)})")

    # Season compatibility
    suitable_seasons = conditions.get("season", [])
    if suitable_seasons and season not in suitable_seasons:
        risk_score += 20
        risk_factors.append(f"{season} is not the recommended season for {crop}")

    # NPK deficiency
    n_range = conditions.get("n", (0, 200))
    p_range = conditions.get("p", (0, 100))
    k_range = conditions.get("k", (0, 200))
    if n < n_range[0]:
        risk_score += 8
        risk_factors.append(f"Nitrogen ({n:.0f}) below minimum requirement ({n_range[0]})")
    if p < p_range[0]:
        risk_score += 8
        risk_factors.append(f"Phosphorus ({p:.0f}) below minimum requirement ({p_range[0]})")
    if k < k_range[0]:
        risk_score += 8
        risk_factors.append(f"Potassium ({k:.0f}) below minimum requirement ({k_range[0]})")

    # State crop suitability
    state_info = STATES_DATA.get(state, {})
    if crop not in state_info.get("major_crops", []):
        risk_score += 5
        risk_factors.append(f"{crop} is not among the major crops of {state}")

    # Classify risk
    risk_score = min(100, risk_score)
    if risk_score <= 25:
        risk_level = "Low"
    elif risk_score <= 55:
        risk_level = "Moderate"
    else:
        risk_level = "High"

    if not risk_factors:
        risk_factors.append("All conditions appear favorable for this crop")

    return {
        "risk_level": risk_level,
        "risk_score": risk_score,
        "factors": risk_factors
    }

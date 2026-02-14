"""
Rule-based Predictor for BharatAgri AI (Vercel-compatible).
Uses CROP_CONDITIONS data for predictions — zero heavy ML dependencies.
"""
import math
import random
from app.data.india_data import CROP_CONDITIONS, CROP_AVG_YIELDS, STATES_DATA, SOIL_CHARACTERISTICS


def _score_crop(crop, conditions, n, p, k, temp, humidity, ph, rainfall, soil_type, state, season):
    """Score how well input conditions match a crop's ideal range. Returns 0-100."""
    score = 0
    max_score = 0

    def range_score(val, low, high, weight=1.0):
        """Score value within range: 100 if inside, decays outside."""
        nonlocal score, max_score
        max_score += weight * 100
        if low <= val <= high:
            score += weight * 100
        else:
            mid = (low + high) / 2
            span = (high - low) / 2 if high != low else 1
            dist = abs(val - mid) / span
            score += weight * max(0, 100 - dist * 25)

    # Core agro parameters
    if "temp" in conditions:
        range_score(temp, *conditions["temp"], weight=2.0)
    if "rainfall" in conditions:
        range_score(rainfall, *conditions["rainfall"], weight=2.0)
    if "ph" in conditions:
        range_score(ph, *conditions["ph"], weight=1.5)
    if "humidity" in conditions:
        range_score(humidity, *conditions["humidity"], weight=1.0)
    if "n" in conditions:
        range_score(n, *conditions["n"], weight=1.2)
    if "p" in conditions:
        range_score(p, *conditions["p"], weight=1.2)
    if "k" in conditions:
        range_score(k, *conditions["k"], weight=1.2)

    # Soil type match (big bonus)
    max_score += 200
    if "soil" in conditions and soil_type in conditions["soil"]:
        score += 200

    # Season match (big bonus)
    max_score += 200
    if "season" in conditions and season in conditions["season"]:
        score += 200

    # State crop bonus
    state_info = STATES_DATA.get(state, {})
    max_score += 100
    if crop in state_info.get("major_crops", []):
        score += 100

    return (score / max_score * 100) if max_score > 0 else 50


def _generate_crop_explanation(crop, n, p, k, temp, humidity, ph, rainfall, soil_type, state, season):
    """Generate human-readable explanation for crop recommendation."""
    conditions = CROP_CONDITIONS.get(crop, {})
    reasons = []

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
        n_range = conditions.get("n", (0, 999))
        if n_range[0] <= n <= n_range[1]:
            reasons.append(f"nitrogen level ({n:.0f}) is optimal")

    if not reasons:
        reasons.append("overall soil and climate conditions are compatible")

    state_info = STATES_DATA.get(state, {})
    if crop in state_info.get("major_crops", []):
        reasons.append(f"it is a major crop grown in {state}")

    return f"{crop} is recommended because " + ", ".join(reasons[:4]) + "."


def predict_crop(n, p, k, temperature, humidity, ph, rainfall, soil_type, state, season):
    """Predict top 3 recommended crops with scores and explanations."""
    scores = {}
    for crop, conditions in CROP_CONDITIONS.items():
        scores[crop] = _score_crop(
            crop, conditions, n, p, k, temperature, humidity, ph, rainfall,
            soil_type, state, season
        )

    # Sort by score descending, take top 3
    ranked = sorted(scores.items(), key=lambda x: -x[1])[:3]

    # Normalize top scores to probabilities
    total = sum(s for _, s in ranked) or 1
    results = []
    for crop, raw_score in ranked:
        explanation = _generate_crop_explanation(
            crop, n, p, k, temperature, humidity, ph, rainfall,
            soil_type, state, season
        )
        results.append({
            "crop": crop,
            "probability": round(raw_score / total * 100, 1),
            "explanation": explanation
        })

    # Feature importance (static, based on agronomic significance)
    feature_importance = {
        "Season": 22.0, "Temperature": 15.0, "Rainfall": 15.0,
        "Soil Type": 14.0, "pH Level": 10.0, "Nitrogen (N)": 8.0,
        "Phosphorus (P)": 6.0, "Potassium (K)": 6.0,
        "Humidity": 5.0, "State": 4.0
    }

    return {
        "recommendations": results,
        "feature_importance": feature_importance
    }


def predict_yield(state, district, crop, season, area, rainfall, temperature):
    """Predict crop yield using rule-based estimation from avg yields + conditions."""
    base_yield = CROP_AVG_YIELDS.get(crop, 2.0)
    conditions = CROP_CONDITIONS.get(crop, {})
    multiplier = 1.0

    # Adjust by temperature fit
    if "temp" in conditions:
        t_low, t_high = conditions["temp"]
        t_mid = (t_low + t_high) / 2
        if t_low <= temperature <= t_high:
            closeness = 1 - abs(temperature - t_mid) / ((t_high - t_low) / 2 + 1)
            multiplier *= 0.9 + 0.2 * closeness
        else:
            multiplier *= 0.7

    # Adjust by rainfall fit
    if "rainfall" in conditions:
        r_low, r_high = conditions["rainfall"]
        if r_low <= rainfall <= r_high:
            multiplier *= 1.05
        else:
            multiplier *= 0.8

    # Season match
    if "season" in conditions and season in conditions["season"]:
        multiplier *= 1.05
    else:
        multiplier *= 0.85

    # State major crop boost
    state_info = STATES_DATA.get(state, {})
    if crop in state_info.get("major_crops", []):
        multiplier *= 1.1

    # Small random variation for realism
    random.seed(hash(f"{state}{district}{crop}{season}{area}"))
    multiplier *= random.uniform(0.95, 1.05)

    predicted_yield = max(0.1, base_yield * multiplier)
    total_production = predicted_yield * area
    yield_diff = ((predicted_yield - base_yield) / base_yield) * 100

    return {
        "predicted_yield": round(predicted_yield, 2),
        "total_production": round(total_production, 2),
        "state_average_yield": round(base_yield, 2),
        "yield_difference_percent": round(yield_diff, 1),
        "unit": "tons/hectare"
    }


def calculate_risk(n, p, k, ph, temperature, humidity, rainfall, soil_type, state, season, crop):
    """Calculate risk score using rule-based approach."""
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

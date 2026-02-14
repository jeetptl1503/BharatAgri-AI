"""
Synthetic dataset generator for BharatAgri AI models.
Generates realistic Indian agriculture data for crop recommendation and yield prediction.
"""
import numpy as np
import pandas as pd
import os
from app.data.india_data import (
    STATES_DATA, SOIL_CHARACTERISTICS, CROP_CONDITIONS,
    ALL_CROPS, SEASONS, CROP_AVG_YIELDS
)

np.random.seed(42)


def generate_crop_recommendation_dataset(n_samples=8000):
    """Generate crop recommendation dataset with state-wise variability."""
    data = []
    states = list(STATES_DATA.keys())

    for _ in range(n_samples):
        state = np.random.choice(states)
        state_info = STATES_DATA[state]
        soil_type = np.random.choice(state_info["soil_types"])
        soil_char = SOIL_CHARACTERISTICS[soil_type]
        season = np.random.choice(SEASONS)
        climate = state_info["climate"]

        # Generate soil nutrients based on soil type
        n = np.random.uniform(*soil_char["n_range"]) * np.random.uniform(0.3, 1.2)
        p = np.random.uniform(*soil_char["p_range"]) * np.random.uniform(0.4, 1.3)
        k = np.random.uniform(*soil_char["k_range"]) * np.random.uniform(0.3, 1.2)
        ph = np.random.uniform(*soil_char["ph_range"])

        # Climate based on state
        temperature = np.random.uniform(climate["temp_min"], climate["temp_max"])
        humidity = np.random.uniform(climate["humidity_min"], climate["humidity_max"])
        rainfall = np.random.uniform(climate["rainfall_min"], climate["rainfall_max"])

        # Determine best crop based on conditions
        best_crop = _find_best_crop(n, p, k, ph, temperature, humidity, rainfall, soil_type, season, state_info["major_crops"])

        data.append({
            "N": round(n, 2),
            "P": round(p, 2),
            "K": round(k, 2),
            "temperature": round(temperature, 2),
            "humidity": round(humidity, 2),
            "ph": round(ph, 2),
            "rainfall": round(rainfall, 2),
            "soil_type": soil_type,
            "state": state,
            "season": season,
            "crop": best_crop
        })

    return pd.DataFrame(data)


def _find_best_crop(n, p, k, ph, temp, humidity, rainfall, soil_type, season, major_crops):
    """Find the best matching crop based on conditions."""
    best_score = -1
    best_crop = "Rice"

    for crop in ALL_CROPS:
        conditions = CROP_CONDITIONS.get(crop)
        if not conditions:
            continue

        score = 0
        # Season match
        if season in conditions["season"]:
            score += 3
        else:
            continue

        # Soil match
        if soil_type in conditions["soil"]:
            score += 2

        # Nutrient scoring
        n_mid = (conditions["n"][0] + conditions["n"][1]) / 2
        p_mid = (conditions["p"][0] + conditions["p"][1]) / 2
        k_mid = (conditions["k"][0] + conditions["k"][1]) / 2

        score += max(0, 1 - abs(n - n_mid) / n_mid)
        score += max(0, 1 - abs(p - p_mid) / p_mid)
        score += max(0, 1 - abs(k - k_mid) / k_mid)

        # Climate scoring
        if conditions["temp"][0] <= temp <= conditions["temp"][1]:
            score += 1.5
        if conditions["humidity"][0] <= humidity <= conditions["humidity"][1]:
            score += 1.0
        if conditions["rainfall"][0] <= rainfall <= conditions["rainfall"][1]:
            score += 1.5
        if conditions["ph"][0] <= ph <= conditions["ph"][1]:
            score += 1.0

        # Bonus for major crops of the state
        if crop in major_crops:
            score += 1.5

        # Add small randomness
        score += np.random.uniform(0, 0.5)

        if score > best_score:
            best_score = score
            best_crop = crop

    return best_crop


def generate_yield_dataset(n_samples=5000):
    """Generate yield prediction dataset with state-wise variability."""
    data = []
    states = list(STATES_DATA.keys())

    for _ in range(n_samples):
        state = np.random.choice(states)
        state_info = STATES_DATA[state]
        district = np.random.choice(state_info["districts"])
        crop = np.random.choice(state_info["major_crops"])
        season = np.random.choice(SEASONS)
        climate = state_info["climate"]

        area = np.random.uniform(0.5, 50.0)  # hectares
        rainfall = np.random.uniform(climate["rainfall_min"], climate["rainfall_max"])
        temperature = np.random.uniform(climate["temp_min"], climate["temp_max"])

        # Base yield from national average
        base_yield = CROP_AVG_YIELDS.get(crop, 2.0)

        # State and climate adjustments
        rainfall_opt = (CROP_CONDITIONS.get(crop, {}).get("rainfall", (800, 1200)))
        rain_mid = (rainfall_opt[0] + rainfall_opt[1]) / 2
        rain_factor = max(0.5, 1 - abs(rainfall - rain_mid) / (rain_mid * 2))

        temp_opt = (CROP_CONDITIONS.get(crop, {}).get("temp", (20, 30)))
        temp_mid = (temp_opt[0] + temp_opt[1]) / 2
        temp_factor = max(0.5, 1 - abs(temperature - temp_mid) / (temp_mid * 2))

        # Calculate yield
        yield_val = base_yield * rain_factor * temp_factor * np.random.uniform(0.7, 1.3)
        production = yield_val * area

        data.append({
            "state": state,
            "district": district,
            "crop": crop,
            "season": season,
            "area": round(area, 2),
            "rainfall": round(rainfall, 2),
            "temperature": round(temperature, 2),
            "production": round(production, 2),
            "yield": round(yield_val, 2)
        })

    return pd.DataFrame(data)


def save_datasets():
    """Generate and save all datasets."""
    data_dir = os.path.join(os.path.dirname(__file__))

    print("Generating crop recommendation dataset...")
    crop_df = generate_crop_recommendation_dataset(8000)
    crop_df.to_csv(os.path.join(data_dir, "crop_recommendation.csv"), index=False)
    print(f"  Saved {len(crop_df)} samples. Crops: {crop_df['crop'].nunique()}")

    print("Generating yield dataset...")
    yield_df = generate_yield_dataset(5000)
    yield_df.to_csv(os.path.join(data_dir, "yield_data.csv"), index=False)
    print(f"  Saved {len(yield_df)} samples.")

    print("Datasets generated successfully!")
    return crop_df, yield_df


if __name__ == "__main__":
    save_datasets()

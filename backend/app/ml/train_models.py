"""
ML model training pipeline for BharatAgri AI.
Trains crop recommendation, yield prediction, and risk scoring models.
"""
import os
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

from app.data.generate_datasets import save_datasets

MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "trained_models")
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def ensure_dirs():
    os.makedirs(MODEL_DIR, exist_ok=True)


def train_crop_recommendation_model():
    """Train RandomForestClassifier for crop recommendation."""
    print("\n=== Training Crop Recommendation Model ===")

    csv_path = os.path.join(DATA_DIR, "crop_recommendation.csv")
    if not os.path.exists(csv_path):
        print("Dataset not found. Generating...")
        save_datasets()

    df = pd.read_csv(csv_path)

    # Encode categorical features
    soil_encoder = LabelEncoder()
    state_encoder = LabelEncoder()
    season_encoder = LabelEncoder()
    crop_encoder = LabelEncoder()

    df["soil_type_enc"] = soil_encoder.fit_transform(df["soil_type"])
    df["state_enc"] = state_encoder.fit_transform(df["state"])
    df["season_enc"] = season_encoder.fit_transform(df["season"])
    df["crop_enc"] = crop_encoder.fit_transform(df["crop"])

    feature_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall",
                    "soil_type_enc", "state_enc", "season_enc"]
    feature_names = ["Nitrogen (N)", "Phosphorus (P)", "Potassium (K)", "Temperature",
                     "Humidity", "pH Level", "Rainfall", "Soil Type", "State", "Season"]

    X = df[feature_cols].values
    y = df["crop_enc"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(
        n_estimators=50,
        max_depth=12,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"  Accuracy: {accuracy:.4f}")

    # Feature importances
    importances = dict(zip(feature_names, model.feature_importances_))
    print(f"  Top features: {sorted(importances.items(), key=lambda x: -x[1])[:5]}")

    # Save model and encoders
    ensure_dirs()
    joblib.dump(model, os.path.join(MODEL_DIR, "crop_model.joblib"), compress=3)
    joblib.dump(soil_encoder, os.path.join(MODEL_DIR, "soil_encoder.joblib"))
    joblib.dump(state_encoder, os.path.join(MODEL_DIR, "state_encoder.joblib"))
    joblib.dump(season_encoder, os.path.join(MODEL_DIR, "season_encoder.joblib"))
    joblib.dump(crop_encoder, os.path.join(MODEL_DIR, "crop_encoder.joblib"))
    joblib.dump(feature_names, os.path.join(MODEL_DIR, "feature_names.joblib"))

    print("  Model saved successfully!")
    return model, accuracy


def train_yield_prediction_model():
    """Train GradientBoostingRegressor for yield prediction."""
    print("\n=== Training Yield Prediction Model ===")

    csv_path = os.path.join(DATA_DIR, "yield_data.csv")
    if not os.path.exists(csv_path):
        save_datasets()

    df = pd.read_csv(csv_path)

    # Encode categorical features
    yield_state_encoder = LabelEncoder()
    yield_crop_encoder = LabelEncoder()
    yield_season_encoder = LabelEncoder()
    yield_district_encoder = LabelEncoder()

    df["state_enc"] = yield_state_encoder.fit_transform(df["state"])
    df["crop_enc"] = yield_crop_encoder.fit_transform(df["crop"])
    df["season_enc"] = yield_season_encoder.fit_transform(df["season"])
    df["district_enc"] = yield_district_encoder.fit_transform(df["district"])

    feature_cols = ["state_enc", "district_enc", "crop_enc", "season_enc",
                    "area", "rainfall", "temperature"]
    yield_feature_names = ["State", "District", "Crop", "Season",
                           "Area (hectares)", "Rainfall", "Temperature"]

    X = df[feature_cols].values
    y = df["yield"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = GradientBoostingRegressor(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        min_samples_split=5,
        random_state=42
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    print(f"  RMSE: {rmse:.4f}")
    print(f"  R² Score: {r2:.4f}")

    # Save
    ensure_dirs()
    joblib.dump(model, os.path.join(MODEL_DIR, "yield_model.joblib"), compress=3)
    joblib.dump(yield_state_encoder, os.path.join(MODEL_DIR, "yield_state_encoder.joblib"))
    joblib.dump(yield_crop_encoder, os.path.join(MODEL_DIR, "yield_crop_encoder.joblib"))
    joblib.dump(yield_season_encoder, os.path.join(MODEL_DIR, "yield_season_encoder.joblib"))
    joblib.dump(yield_district_encoder, os.path.join(MODEL_DIR, "yield_district_encoder.joblib"))
    joblib.dump(yield_feature_names, os.path.join(MODEL_DIR, "yield_feature_names.joblib"))

    print("  Model saved successfully!")
    return model, r2


def train_all():
    """Train all models."""
    print("=" * 60)
    print("BharatAgri AI - Model Training Pipeline")
    print("=" * 60)

    save_datasets()
    crop_model, crop_acc = train_crop_recommendation_model()
    yield_model, yield_r2 = train_yield_prediction_model()

    print("\n" + "=" * 60)
    print("Training Complete!")
    print(f"  Crop Model Accuracy: {crop_acc:.4f}")
    print(f"  Yield Model R²: {yield_r2:.4f}")
    print("=" * 60)


if __name__ == "__main__":
    train_all()

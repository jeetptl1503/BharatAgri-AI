"""
Prediction routes for BharatAgri AI.
Crop recommendation, yield prediction, and risk analysis endpoints.
"""
import json
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional
from app.models.database import get_db, PredictionHistory, User
from app.routes.auth import get_current_user
from app.ml.predictor import predict_crop, predict_yield, calculate_risk

router = APIRouter(prefix="/api/predict", tags=["Predictions"])


class CropInput(BaseModel):
    n: float
    p: float
    k: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    soil_type: str
    state: str
    season: str


class YieldInput(BaseModel):
    state: str
    district: str
    crop: str
    season: str
    area: float
    rainfall: float
    temperature: float


class RiskInput(BaseModel):
    n: float
    p: float
    k: float
    ph: float
    temperature: float
    humidity: float
    rainfall: float
    soil_type: str
    state: str
    season: str
    crop: str


class FullPredictionInput(BaseModel):
    n: float
    p: float
    k: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float
    soil_type: str
    state: str
    district: str
    season: str
    area: float = 1.0


@router.post("/crop")
def recommend_crop(
    data: CropInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        result = predict_crop(
            data.n, data.p, data.k, data.temperature,
            data.humidity, data.ph, data.rainfall,
            data.soil_type, data.state, data.season
        )

        # Save to history
        history = PredictionHistory(
            user_id=current_user.id,
            prediction_type="crop",
            input_data=data.model_dump(),
            result_data=result,
            state=data.state
        )
        db.add(history)
        db.commit()

        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@router.post("/yield")
def predict_yield_endpoint(
    data: YieldInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        result = predict_yield(
            data.state, data.district, data.crop,
            data.season, data.area, data.rainfall, data.temperature
        )

        history = PredictionHistory(
            user_id=current_user.id,
            prediction_type="yield",
            input_data=data.model_dump(),
            result_data=result,
            state=data.state,
            district=data.district
        )
        db.add(history)
        db.commit()

        return result
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@router.post("/risk")
def analyze_risk(
    data: RiskInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        result = calculate_risk(
            data.n, data.p, data.k, data.ph,
            data.temperature, data.humidity, data.rainfall,
            data.soil_type, data.state, data.season, data.crop
        )

        history = PredictionHistory(
            user_id=current_user.id,
            prediction_type="risk",
            input_data=data.model_dump(),
            result_data=result,
            state=data.state
        )
        db.add(history)
        db.commit()

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Risk analysis error: {str(e)}")


@router.post("/full")
def full_prediction(
    data: FullPredictionInput,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Run full prediction: crop recommendation + yield + risk analysis."""
    try:
        # Step 1: Get crop recommendations
        crop_result = predict_crop(
            data.n, data.p, data.k, data.temperature,
            data.humidity, data.ph, data.rainfall,
            data.soil_type, data.state, data.season
        )

        top_crop = crop_result["recommendations"][0]["crop"]

        # Step 2: Predict yield for top crop
        yield_result = predict_yield(
            data.state, data.district, top_crop,
            data.season, data.area, data.rainfall, data.temperature
        )

        # Step 3: Risk analysis for top crop
        risk_result = calculate_risk(
            data.n, data.p, data.k, data.ph,
            data.temperature, data.humidity, data.rainfall,
            data.soil_type, data.state, data.season, top_crop
        )

        full_result = {
            "crop_recommendations": crop_result,
            "yield_prediction": yield_result,
            "risk_analysis": risk_result
        }

        # Save to history
        history = PredictionHistory(
            user_id=current_user.id,
            prediction_type="full",
            input_data=data.model_dump(),
            result_data=full_result,
            state=data.state,
            district=data.district
        )
        db.add(history)
        db.commit()

        return full_result
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@router.get("/history")
def get_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    history = db.query(PredictionHistory).filter(
        PredictionHistory.user_id == current_user.id
    ).order_by(PredictionHistory.created_at.desc()).limit(50).all()

    return [
        {
            "id": h.id,
            "prediction_type": h.prediction_type,
            "input_data": h.input_data,
            "result_data": h.result_data,
            "state": h.state,
            "district": h.district,
            "created_at": h.created_at.isoformat()
        }
        for h in history
    ]

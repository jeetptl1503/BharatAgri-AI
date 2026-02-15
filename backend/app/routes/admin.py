"""
Admin routes for BharatAgri AI.
Protected by ADMIN_SECRET_KEY — developer-only access.
"""
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.database import get_db, User, PredictionHistory, ChatHistory
from app.config import settings

router = APIRouter(prefix="/api/admin", tags=["Admin"])


def verify_admin(x_admin_key: str = Header(...)):
    """Verify admin secret key from request header."""
    if x_admin_key != settings.ADMIN_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid admin key")
    return True


@router.get("/stats")
def get_stats(
    _: bool = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    """Get overview stats: total users, predictions, chats."""
    total_users = db.query(func.count(User.id)).scalar()
    total_predictions = db.query(func.count(PredictionHistory.id)).scalar()
    total_chats = db.query(func.count(ChatHistory.id)).scalar()

    # Predictions by type
    pred_by_type = db.query(
        PredictionHistory.prediction_type,
        func.count(PredictionHistory.id)
    ).group_by(PredictionHistory.prediction_type).all()

    return {
        "total_users": total_users,
        "total_predictions": total_predictions,
        "total_chats": total_chats,
        "predictions_by_type": {t: c for t, c in pred_by_type}
    }


@router.get("/users")
def get_all_users(
    _: bool = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    """Get all registered users."""
    users = db.query(User).order_by(User.created_at.desc()).all()

    return [
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "state": u.state,
            "language": u.language,
            "created_at": u.created_at.isoformat() if u.created_at else None,
            "prediction_count": db.query(func.count(PredictionHistory.id)).filter(
                PredictionHistory.user_id == u.id
            ).scalar()
        }
        for u in users
    ]


@router.get("/predictions")
def get_all_predictions(
    _: bool = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    """Get all predictions with user info."""
    predictions = db.query(PredictionHistory).order_by(
        PredictionHistory.created_at.desc()
    ).limit(200).all()

    results = []
    for p in predictions:
        user = db.query(User).filter(User.id == p.user_id).first()
        results.append({
            "id": p.id,
            "user_name": user.name if user else "Unknown",
            "user_email": user.email if user else "Unknown",
            "prediction_type": p.prediction_type,
            "input_data": p.input_data,
            "result_data": p.result_data,
            "state": p.state,
            "district": p.district,
            "created_at": p.created_at.isoformat() if p.created_at else None
        })

    return results


@router.get("/chats")
def get_all_chats(
    _: bool = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    """Get all chat messages with user info."""
    chats = db.query(ChatHistory).order_by(
        ChatHistory.created_at.desc()
    ).limit(200).all()

    results = []
    for c in chats:
        user = db.query(User).filter(User.id == c.user_id).first()
        results.append({
            "id": c.id,
            "user_name": user.name if user else "Unknown",
            "user_email": user.email if user else "Unknown",
            "message": c.message,
            "response": c.response,
            "language": c.language,
            "created_at": c.created_at.isoformat() if c.created_at else None
        })

    return results

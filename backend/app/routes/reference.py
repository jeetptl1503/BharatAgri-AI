"""
Reference data routes for BharatAgri AI.
Provides state, district, soil type, and climate reference data.
"""
from fastapi import APIRouter
from app.data.india_data import STATES_DATA, SOIL_TYPES, SOIL_CHARACTERISTICS, SEASONS

router = APIRouter(prefix="/api/reference", tags=["Reference Data"])


@router.get("/states")
def get_states():
    """Get list of all supported states."""
    return {
        "states": sorted(list(STATES_DATA.keys()))
    }


@router.get("/districts/{state}")
def get_districts(state: str):
    """Get districts for a given state."""
    state_info = STATES_DATA.get(state)
    if not state_info:
        return {"districts": [], "error": "State not found"}
    return {
        "state": state,
        "districts": sorted(state_info["districts"])
    }


@router.get("/soil-types")
def get_soil_types():
    """Get all soil types with characteristics."""
    return {
        "soil_types": [
            {
                "name": soil,
                "description": SOIL_CHARACTERISTICS[soil]["description"],
                "ph_range": SOIL_CHARACTERISTICS[soil]["ph_range"],
                "n_range": SOIL_CHARACTERISTICS[soil]["n_range"],
                "p_range": SOIL_CHARACTERISTICS[soil]["p_range"],
                "k_range": SOIL_CHARACTERISTICS[soil]["k_range"]
            }
            for soil in SOIL_TYPES
        ]
    }


@router.get("/soil-types/{state}")
def get_state_soil_types(state: str):
    """Get soil types available in a specific state."""
    state_info = STATES_DATA.get(state)
    if not state_info:
        return {"soil_types": SOIL_TYPES}
    return {
        "state": state,
        "soil_types": state_info["soil_types"]
    }


@router.get("/climate/{state}")
def get_climate(state: str):
    """Get climate defaults for a state."""
    state_info = STATES_DATA.get(state)
    if not state_info:
        return {"error": "State not found"}
    return {
        "state": state,
        "climate": state_info["climate"],
        "major_crops": state_info["major_crops"]
    }


@router.get("/seasons")
def get_seasons():
    """Get available seasons."""
    return {
        "seasons": [
            {"name": "Kharif", "description": "Monsoon season (June-October)", "months": "Jun-Oct"},
            {"name": "Rabi", "description": "Winter season (October-March)", "months": "Oct-Mar"},
            {"name": "Zaid", "description": "Summer season (March-June)", "months": "Mar-Jun"}
        ]
    }

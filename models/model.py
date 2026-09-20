from pydantic import BaseModel
from typing import List, Optional

class WeatherData(BaseModel):
    condition: str  # e.g., 'sunny', 'rainy'
    wind_speed_kmh: float
    temperature: float

class Activity(BaseModel):
    name: str
    is_outdoor: bool

class RecommendationResponse(BaseModel):
    activities: List[Activity]
    alerts: Optional[List[str]] = []
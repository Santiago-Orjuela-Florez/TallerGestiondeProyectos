from fastapi import FastAPI
from models.model import WeatherData, RecommendationResponse
from service.service import RecommendationEngine

app = FastAPI(title="Tourism Weather Recommender")
engine = RecommendationEngine()

@app.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(weather: WeatherData):
    """
    Endpoint que consume los datos del clima y retorna actividades.
    En un entorno real, este microservicio haría un request HTTP a la API del clima
    basado en lat/lon. Por simplicidad del prototipo, recibe el payload directamente.
    """
    return engine.get_recommendations(weather)
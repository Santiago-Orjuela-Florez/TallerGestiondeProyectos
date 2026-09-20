from models.model import WeatherData, RecommendationResponse
from core.rules import RecommendationRule, SunnyWeatherRule, RainyWeatherRule, HighWindSafetyRule

class RecommendationEngine:
    def __init__(self):
        self.rules: list[RecommendationRule] = [
            SunnyWeatherRule(),
            RainyWeatherRule(),
            HighWindSafetyRule() 
        ]

    def get_recommendations(self, weather: WeatherData) -> RecommendationResponse:
        activities = []
        for rule in self.rules:
            activities = rule.apply(weather, activities)
        
        alerts = []
        if weather.wind_speed_kmh > 50:
            alerts.append("ALERTA DE SEGURIDAD: Vientos huracanados. Actividades al aire libre suspendidas.")


        return RecommendationResponse(activities=activities, alerts=alerts)
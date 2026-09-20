from abc import ABC, abstractmethod
from models.model import WeatherData, Activity

class RecommendationRule(ABC):
    @abstractmethod
    def apply(self, weather: WeatherData, current_activities: list[Activity]) -> list[Activity]:
        pass

class SunnyWeatherRule(RecommendationRule):
    def apply(self, weather: WeatherData, current_activities: list[Activity]) -> list[Activity]:
        if weather.condition == 'sunny':
            current_activities.append(Activity(name="City Tour Caminando", is_outdoor=True))
            current_activities.append(Activity(name="Visita a Museo", is_outdoor=False))
        return current_activities

class RainyWeatherRule(RecommendationRule):
    def apply(self, weather: WeatherData, current_activities: list[Activity]) -> list[Activity]:
        if weather.condition == 'rainy':
            current_activities.append(Activity(name="Cata de Vinos", is_outdoor=False))
            current_activities.append(Activity(name="Tour de Museos", is_outdoor=False))
        return current_activities

# --- NUEVO REQUERIMIENTO DEL CLIENTE ---
class HighWindSafetyRule(RecommendationRule):
    def apply(self, weather: WeatherData, current_activities: list[Activity]) -> list[Activity]:
        if weather.wind_speed_kmh > 50:
            # Filtra todas las actividades al aire libre
            return [act for act in current_activities if not act.is_outdoor]
        return current_activities
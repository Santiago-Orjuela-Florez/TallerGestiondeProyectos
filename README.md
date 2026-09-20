# Tourism Weather Recommender API 

Este es un microservicio desarrollado con FastAPI para una empresa de turismo. El sistema consume datos meteorológicos y recomienda actividades a los viajeros según el pronóstico. Además, implementa reglas de seguridad críticas para proteger a los turistas en condiciones climáticas extremas.

Proyecto desarrollado para la materia de **Gestión de Proyectos**.

## Características Principales

- **Recomendaciones Dinámicas:** Sugiere actividades basadas en el clima actual (soleado, lluvioso, etc.).

- **Filtro de Seguridad (Requerimiento Crítico):** Si la velocidad del viento supera los 50 km/h, el sistema bloquea automáticamente cualquier sugerencia de actividad al aire libre y emite una alerta de seguridad.

- **Arquitectura Escalable:** Utiliza un Motor de Reglas (Patrón Strategy) que permite agregar nuevas restricciones climáticas o de negocio sin modificar el código base (cumpliendo con el principio _Open/Closed_).

## Estructura del Proyecto

```
tourism-weather-api/
├── core/
│   ├── __init__.py
│   ├── models.py       # Modelos de datos (Pydantic)
│   └── rules.py        # Motor de reglas y lógicas de clima/seguridad
├── service/
│   ├── __init__.py
│   └── service.py      # Orquestador del pipeline de recomendaciones
├── main.py             # Punto de entrada de la aplicación FastAPI
└── README.md

```

## Instalación y Configuración

Asegúrate de tener Python 3.8 o superior instalado en tu sistema.

1. **Clonar el repositorio (o ubicar la carpeta del proyecto):**

   ```
   git clone <URL_DEL_REPOSITORIO>
   cd tourism-weather-api

   ```

2. **Crear y activar un entorno virtual:**
   - En Windows (PowerShell):

     ```
     python -m venv venv
     .\venv\Scripts\Activate

     ```

   - En macOS/Linux:

     ```
     python3 -m venv venv
     source venv/bin/activate

     ```

3. **Instalar las dependencias:**

   ```
   pip install fastapi uvicorn pydantic

   ```

4. **Ejecutar el servidor:**

   ```
   uvicorn main:app --reload

   ```

   _El servidor se iniciará en `http://127.0.0.1:8000`_

## Uso de la API

La forma más sencilla de probar y explorar la API es a través de la interfaz interactiva de Swagger que provee FastAPI.

Con el servidor corriendo, abre tu navegador y visita: [**http://127.0.0.1:8000/docs**](http://127.0.0.1:8000/docs?utm_source=gemini)

### Endpoint Principal

`POST /recommendations`

Recibe las condiciones climáticas actuales y retorna una lista de actividades filtradas junto con posibles alertas de seguridad.

**Ejemplo de Petición (Request Body - JSON):**
Simulando un día soleado pero con vientos peligrosos (> 50 km/h):

```
{
  "condition": "sunny",
  "wind_speed_kmh": 65.5,
  "temperature": 28.0
}

```

**Ejemplo de Respuesta (Response Body - JSON):**
El sistema bloquea el "City Tour Caminando" (al aire libre) y emite la alerta de marketing.

```
{
  "activities": [
    {
      "name": "Visita a Museo",
      "is_outdoor": false
    }
  ],
  "alerts": [
    "ALERTA DE SEGURIDAD: Vientos huracanados. Actividades al aire libre suspendidas."
  ]
}

```

## Justificación Técnica del Diseño

Durante el desarrollo, el cliente solicitó un cambio crítico: bloquear actividades al aire libre por vientos fuertes. Para evitar el _Código Espagueti_ y no romper las reglas existentes, el equipo implementó un **Motor de Reglas**.

El flujo de información pasa por un pipeline:

1. `SunnyWeatherRule` / `RainyWeatherRule`: Agregan actividades base según el clima.

2. `HighWindSafetyRule`: Intercepta la lista y filtra todo lo que sea `is_outdoor = true` si detecta peligro, añadiendo además la alerta.

Este enfoque asegura que el sistema sea tolerante a cambios de alcance (Scope Creep) durante la gestión del proyecto.

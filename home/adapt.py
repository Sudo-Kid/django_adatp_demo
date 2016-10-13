from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

engine = IntentDeterminationEngine()

weather_keyword = [
    "weather"
]

for wk in weather_keyword:
    engine.register_entity(wk, "WeatherKeyword")

weather_types = [
    "snow",
    "rain",
    "wind",
    "sleet",
    "sun"
]

for wt in weather_types:
    engine.register_entity(wt, "WeatherType")

locations = [
    "Seattle",
    "San Francisco",
    "Tokyo",
    "Vancouver"
]

for loc in locations:
    engine.register_entity(loc, "Location")

weather_intent = IntentBuilder("WeatherIntent")\
    .require("WeatherKeyword")\
    .optionally("WeatherType")\
    .require("Location")\
    .build()

engine.register_intent_parser(weather_intent)


def get_intent(message):
    for intent in engine.determine_intent(message):
        if intent.get('confidence') > 0:
            return intent

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY") 

settings = Settings()

if __name__ == "__main__":
    print(settings.GROQ_API_KEY)
from langchain.tools import TavilySearchResults
from app.config import settings
import os

os.environ["TAVILY_API_KEY"] = settings.TAVILY_API_KEY

search = TavilySearchResults()
from langchain.tools import TavilySearchResults
from app.config import settings
import os

# set API key
os.environ["TAVILY_API_KEY"] = settings.TAVILY_API_KEY

# create tool
search = TavilySearchResults()
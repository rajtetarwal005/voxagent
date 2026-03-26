from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
# from app.services.whisper_service import speech_to_text
# from app.services.tts_service import text_to_speech

from app.config import settings
from app.tools.calculator import calculator
from app.tools.weather import get_weather
from app.tools.search import search


system_prompt = """
You are an intelligent AI assistant with access to multiple tools.

Your goal is to understand the user's intent and choose the correct tool.

GENERAL BEHAVIOR:
- Understand meaning even if there are spelling mistakes or bad grammar.
- Do not depend on exact wording; focus on intent.
- Interpret unclear queries in the most logical way.

TOOL SELECTION RULES:

1. Weather Tool:
- Use this tool whenever the user is asking about weather conditions.
- This includes questions about temperature, rain, heat, cold, climate, or general weather.
- Extract the city name even if it is misspelled.

2. Calculator Tool:
- Use this tool for any mathematical or numerical computation.

3. Search Tool:
- Use this tool for any general knowledge or external information.

REASONING:
- Choose tools based on intent, not keywords.
- You can use multiple tools if needed.

FINAL RESPONSE:
- Give a clean and human-friendly answer.
- Do not show internal steps.
"""

def get_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=settings.GROQ_API_KEY,
        temperature=0
    )
memory = MemorySaver()

def get_agent():
    llm = get_llm()

    tools = [calculator, get_weather, search]

    agent = create_agent(
    llm,    
    tools,
    system_prompt=system_prompt,
    checkpointer=memory
    )

    return agent
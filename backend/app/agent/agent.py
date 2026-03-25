from langchain_groq import ChatGroq
from langchain.agents import create_agent

from app.config import settings
from app.tools.calculator import calculator
from app.tools.weather import get_weather
from app.tools.search import search


def get_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=settings.GROQ_API_KEY,
        temperature=0
    )


def get_agent():
    llm = get_llm()

    tools = [calculator, get_weather, search]

    agent = create_agent(llm, tools)

    return agent


if __name__ == "__main__":
    agent = get_agent()

    query = input("Ask something: ")

    response = agent.invoke({
        "messages": [("user", query)]
    })

    print("\nFinal Answer:\n", response["messages"][-1].content)
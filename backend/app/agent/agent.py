from langchain_groq import ChatGroq
from langchain.agents import create_agent

from app.config import settings
from app.tools.calculator import calculator


def get_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=settings.GROQ_API_KEY,
        temperature=0
    )


def get_agent():
    llm = get_llm()
    
    tools = [calculator]   # 👈 attach tool here
    
    agent = create_agent(llm, tools)
    
    return agent


# test agent
if __name__ == "__main__":
    agent = get_agent()

    response = agent.invoke({
        "messages": [("user", "What is 5 * 10 + 3?")]
    })

    print(response)
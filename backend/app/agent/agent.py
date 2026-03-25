from langchain_groq import ChatGroq
from app.config import settings

def get_llm():
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=settings.GROQ_API_KEY,
        temperature=0
    )
    return llm


if __name__ == "__main__":
    llm = get_llm()
    
    response = llm.invoke("Explain AI in one line")
    print(response.content)
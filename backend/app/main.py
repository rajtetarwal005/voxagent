from fastapi import FastAPI
from app.agent.agent import get_agent
from app.schemas.chat_schema import ChatRequest

app = FastAPI()

# load agent once
agent = get_agent()


@app.get("/")
def home():
    return {"message": "VoxAgent API is running 🚀"}


@app.post("/chat")
def chat(query: ChatRequest):   
    user_input = query.message 

    response = agent.invoke(
        {
            "messages": [("user", user_input)]
        },
        config={
            "configurable": {"thread_id": "1"}
        }
    )

    final_answer = response["messages"][-1].content

    return {"response": final_answer}
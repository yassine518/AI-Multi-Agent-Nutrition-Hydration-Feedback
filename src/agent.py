import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.5
)

class WaterIntakerAgent:
    def __init__(self):
        self.history = []
        
    def analyse_intake(self, intake_ml):
        prompt = f"""
        you are a hydration assistant. The user has consumed {intake_ml} ml of water today.
        provide a hydration status and suggest if they need to drink more water
        """
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content

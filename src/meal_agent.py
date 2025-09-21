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

class MealTrackerAgent:
    def __init__(self):
        pass

    def track_meal(self, meal_data):
        """
        Tracks a meal and its calorie intake and provides feedback.
        """
        meal = meal_data['meal']
        calories = meal_data['calories']
        
        prompt = f"""
        You are a nutrition assistant. The user has consumed a meal: '{meal}' with {calories} calories.
        Provide a brief, encouraging, and informative feedback on their meal choice.
        """
        
        response = llm.invoke([HumanMessage(content=prompt)])
        
        print(f"Tracking meal: {meal_data}")
        return {"status": "success", "message": response.content}

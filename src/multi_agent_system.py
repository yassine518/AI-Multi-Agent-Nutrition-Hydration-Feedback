from src.agent import WaterIntakerAgent
from src.meal_agent import MealTrackerAgent

class MultiAgentSystem:
    def __init__(self):
        self.water_agent = WaterIntakerAgent()
        self.meal_agent = MealTrackerAgent()

    def analyze_health_data(self, water_intake, meal_data):
        water_analysis = self.water_agent.analyse_intake(water_intake)
        meal_analysis = self.meal_agent.track_meal(meal_data)
        
        return {
            "water_analysis": water_analysis,
            "meal_analysis": meal_analysis
        }

if __name__ == "__main__":
    multi_agent_system = MultiAgentSystem()
    
    water_intake = 2000  # Example water intake in ml
    meal_data = {"meal": "Lunch", "calories": 700}  # Example meal data
    
    health_analysis = multi_agent_system.analyze_health_data(water_intake, meal_data)
    
    print("--- Health Analysis ---")
    print(f"Water Intake Analysis: {health_analysis['water_analysis']}")
    print(f"Meal Tracking Analysis: {health_analysis['meal_analysis']}")
    print("-----------------------")

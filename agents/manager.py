from agents.tutor import tutor_agent
from agents.evaluator import evaluator_agent
from agents.recommender import recommender_agent
from agents.search import search_agent
from agents.base import Agent

manager_prompt = open("prompts/manager_prompt.txt").read()

manager_agent = Agent(
    name="C0mpanionManager",
    instructions=manager_prompt,
    tools=[
        tutor_agent.as_tool("TutorAgent", "Menjelaskan konsep AI"),
        evaluator_agent.as_tool("EvaluatorAgent", "Evaluasi pemahaman"),
        recommender_agent.as_tool("RecommenderAgent", "Rencana belajar"),
        search_agent.as_tool("SearchAgent", "Mencari referensi")
    ]
)

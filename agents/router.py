from agents.tutor import tutor_agent
from agents.evaluator import evaluator_agent
from agents.recommender import recommender_agent
from agents.search import search_agent
from agents.base import Runner

async def route_to_agent(input_text: str):
    lowered = input_text.lower()

    if any(keyword in lowered for keyword in [
        "quiz", "test", "soal", "evaluate", "exercise", "questionnaire", "assessment"]):
        agent = evaluator_agent

    elif any(keyword in lowered for keyword in [
        "recommend", "study", "beginner", "where to start", "start learning", "how to begin", "guide", "saran", "pemula"]):
        agent = recommender_agent

    elif any(keyword in lowered for keyword in [
        "search", "lookup", "find", "referensi", "web", "google", "source", "sumber"]):
        agent = search_agent

    elif any(keyword in lowered for keyword in [
        "explain", "what is", "how does", "jelaskan", "apa itu", "describe", "penjelasan", "mengapa", "bagaimana"]):
        agent = tutor_agent

    else:
        agent = tutor_agent

    response = await Runner.run(agent, input_text)
    return agent.name, response




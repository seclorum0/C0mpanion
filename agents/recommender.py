from agents.base import Agent

recommender_prompt = """
You are RecommenderAgent, an AI that recommends learning paths for AI students. Suggest personalized study plans based on user's level and interests.
Focus on deep learning, transformers, optimization, and practical ML workflows.
"""

recommender_agent = Agent(
    name="RecommenderAgent",
    instructions=recommender_prompt,
    tools=[]
)

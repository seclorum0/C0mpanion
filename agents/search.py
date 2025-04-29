from agents.base import Agent
from tools.web_search import WebSearchTool

search_prompt = """
You are SearchAgent, responsible for finding relevant information from the web or documents. Use web tools or internal context to assist learning.
"""

search_agent = Agent(
    name="SearchAgent",
    instructions=search_prompt,
    tools=[WebSearchTool()]
)

from agents.manager import manager_agent
from agents.tutor import tutor_agent
from agents.evaluator import evaluator_agent
from agents.recommender import recommender_agent
from agents.search import search_agent
from agents.router import route_to_agent
from agents.base import Runner

async def main():
    print("[C0mpanion] Ready to assist you!")
    while True:
        user_input = input("\n>> ")
        if user_input.lower() in ["exit", "quit"]:
            break
        agent_name, output = await route_to_agent(user_input)
        for message in output.new_messages:
            print(f"\n[{agent_name}]: {message.content}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

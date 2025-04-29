import httpx
from httpx import ReadTimeout, ConnectError
import asyncio

class Agent:
    def __init__(self, name, instructions, tools=[], output_type=None):
        self.name = name
        self.instructions = instructions
        self.tools = tools
        self.output_type = output_type

    def as_tool(self, tool_name, tool_description):
        return {
            "name": tool_name,
            "description": tool_description,
            "agent": self
        }

class Runner:
    @staticmethod
    async def run(agent, input_text):
        prompt = f"{agent.instructions.strip()}\n\nUser: {input_text}\n\nAssistant:"
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama2",
                        "prompt": prompt,
                        "stream": False,
                    }
                )
                data = response.json()
                if "error" in data:
                    print("[ERROR from Ollama]", data["error"])
                class Msg:
                    def __init__(self, content):
                        self.content = data.get("response", "[No Response]")
                return type("Output", (), {
    "new_messages": [Msg(content=data.get("response", "[No Response]"))]
})
        except (ReadTimeout, ConnectError):
            class Msg:
                def __init__(self, content):
                    self.content = "⚠️ Gagal terhubung. Pastikan Ollama dan model sedang aktif."
            return type("Output", (), {"new_messages": [Msg("⚠️ Tidak bisa terhubung.")]})

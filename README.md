# C0mpanion - AI Learning Assistant

C0mpanion is a multi-agent AI system designed to help users learn about artificial intelligence, machine learning, neural networks, and deep learning. Built on the principles outlined in OpenAI's research on AI agents, C0mpanion utilizes specialized agents to provide a comprehensive learning experience.

## 🤖 Features

- **Multi-Agent Architecture**: System of specialized AI agents working together to assist with learning
- **Natural Language Interface**: Interact with the system using conversational prompts
- **Specialized Support**: Different agents for different learning needs
- **Local Execution**: Runs on your machine using Ollama for inference

## 📋 Agents

C0mpanion consists of several specialized agents:

1. **TutorAgent** - Explains AI and ML concepts clearly with appropriate examples and code snippets
2. **EvaluatorAgent** - Tests knowledge through quizzes and provides constructive feedback
3. **RecommenderAgent** - Suggests personalized learning paths based on user level and interests
4. **SearchAgent** - Retrieves relevant information from the web to augment learning
5. **ManagerAgent** - Routes user requests to the appropriate specialized agent

## 🛠️ Requirements

- Python 3.7+
- [Ollama](https://ollama.ai/) - Used for local model inference
- Required Python packages (see `requirements.txt`)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/C0mpanion.git
   cd C0mpanion
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and run [Ollama](https://ollama.ai/) with the Llama2 model:
   ```bash
   ollama pull llama2
   ollama run llama2
   ```

## 🚀 Usage

1. Start Ollama with the Llama2 model running
2. Run the C0mpanion system:
   ```bash
   python main.py
   ```
3. Interact with the system through the command line interface:
   ```
   >> Explain how transformers work in deep learning
   [TutorAgent]: Transformers are a type of neural network architecture...
   
   >> Give me a quiz on neural networks
   [EvaluatorAgent]: Here's a quick quiz to test your knowledge...
   
   >> Recommend a learning path for AI beginners
   [RecommenderAgent]: For beginners in AI, I recommend starting with...
   ```

## 🧠 How It Works

C0mpanion uses a router system to analyze user input and direct it to the most appropriate specialized agent:

- Questions about concepts are directed to the TutorAgent
- Requests for tests or evaluations go to the EvaluatorAgent
- Requests for learning recommendations go to the RecommenderAgent
- Information lookup requests are handled by the SearchAgent

Each agent is specialized with specific prompts and tools to effectively handle its designated responsibilities.

## 📃 Project Structure

```
C0mpanion/
├── agents/
│   ├── __init__.py
│   ├── base.py           # Base Agent class and Runner for execution
│   ├── evaluator.py      # Agent for testing knowledge
│   ├── manager.py        # Main manager agent
│   ├── recommender.py    # Agent for suggesting learning paths
│   ├── router.py         # Logic for routing requests to agents
│   ├── search.py         # Agent for web searches
│   └── tutor.py          # Agent for explaining concepts
├── prompts/
│   └── manager_prompt.txt # Instructions for the manager agent
├── tools/
│   └── web_search.py     # Tool for web searching
├── main.py               # Application entry point
└── requirements.txt      # Project dependencies
```

## 🛠️ Customization

You can customize the agents' behavior by modifying their respective prompt files. Each agent has specific instructions that guide its responses and behavior.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- Inspired by OpenAI's research on AI agents
- Built using Ollama for local model inference
- Thanks to all contributors and the AI learning community


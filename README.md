## 🔗Lang Chain First App

A simple starter application demonstrating how to build AI-powered workflows using **LangChain** and Python. This project serves as a minimal boilerplate for initializing model calls, managing prompt templates, and invoking chains/agents.

---

 ## Features

- **LLM Integration:** Connects seamlessly to model providers (OpenAI, Anthropic, Google Gemini, Ollama, etc.).
- **Prompt Templating:** Dynamic prompt construction using `ChatPromptTemplate`.
- **Chain & Agent Invocation:** Simple chain pipelines using the LangChain Expression Language (LCEL).
- **Environment Management:** Secure secret management with `.env` files.

---

##  Prerequisites

Before getting started, ensure you have the following installed:

- **Python:** `3.10` or higher
- **Package Manager:** `pip` or `uv`
- **API Key:** An active API key from an AI provider (e.g., [OpenAI](https://platform.openai.com/), [Google AI Studio](https://aistudio.google.com/), or [Anthropic](https://console.anthropic.com/)).

---

##  Getting Started

### 1. Clone the Repository

bash
git clone [https://github.com/your-username/langchain-first-app.git](https://github.com/your-username/langchain-first-app.git)
cd lang chain-first-app
## Create a virtual environment & install packages:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
## Configure environment variables:
Code snippet
GOOGLE_API_KEY=your_gemini_api_key
## Launch the application:
python app.py






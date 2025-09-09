# 🔍 Search Agent with LLM Response

This project is an **AI-powered search assistant** that performs **real-time web searches** and generates **summarized answers** using an LLM (via [Ollama](https://ollama.com/)).

Think of it as a **mini search + answer bot**:

1. Queries Google via [SerpAPI](https://serpapi.com/).
2. Collects top results (title, snippet, URL).
3. Feeds them into a local LLM (e.g., `tinyllama` or `llama2`).
4. Returns a **natural language answer with sources**.

---

## ✨ Features

* 🔑 Uses **SerpAPI** for real web search.
* 🤖 Summarizes results using **Ollama models** (`tinyllama`, `llama2`, etc.).
* 🔒 Secure API key handling via `.env`.
* 📋 Provides **sources & citations** for transparency.
* 🛠️ Modular and easy to extend.

---

## 📂 Project Structure

```
├── .env                  # Stores your API keys securely
├── search_agent.py       # Main search agent code
├── README.md             # Documentation
```

---

## ⚡ How It Works (Pipeline)

```html
flowchart TD
    A[User Query] --> B[Search Web via SerpAPI]
    B --> C[Collect Results (title, snippet, URL)]
    C --> D[Feed Context into LLM (Ollama)]
    D --> E[Generate Final Answer]
    E --> F[Display Answer + Sources]
```

---

## 🚀 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/simple-search-agent.git
cd simple-search-agent
```

### 2. Install Dependencies

```bash
pip install requests python-dotenv ollama
```

### 3. Add API Key

Create a `.env` file:

```
SERPAPI_KEY=your_real_serpapi_key_here
```

> 🔑 Get your free SerpAPI key at [serpapi.com](https://serpapi.com/).

### 4. Run Agent

```bash
python search_agent.py
```

---

## 🧑‍💻 Example Usage

```text
============================================================
QUERY: What is quantum computing?
============================================================
🔍 Searching for: What is quantum computing?
🤖 Generating response...

📋 Response:
Query: What is quantum computing?

Answer: Quantum computing is a new paradigm of computation that uses
quantum mechanics to solve complex problems faster than classical computers.
It relies on qubits, superposition, and entanglement.

Sources:
  - Quantum Computing Explained - IBM Research: https://www.ibm.com/quantum-computing/learn/what-is-quantum-computing/
  - What is Quantum Computing? - Microsoft Azure: https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-quantum-computing/
  - Introduction to Quantum Computing - Wikipedia: https://en.wikipedia.org/wiki/Quantum_computing
```

---

## 🛠️ Tech Stack

* **[Ollama](https://ollama.com/):** Local LLM inference (`tinyllama`, `llama2`, etc.)
* **[SerpAPI](https://serpapi.com/):** Google Search API
* **Python Libraries:**

  * `requests` → API calls
  * `python-dotenv` → Load API key from `.env`
  * `typing` → Type hints

---

## 🌍 Real-World Use Cases

✅ **Research Assistant** – Summarize latest findings with sources.
✅ **Student Helper** – Get quick explanations with citations.
✅ **News Summarizer** – Pull top headlines and generate summaries.
✅ **Business Intelligence** – Gather insights from multiple sources in seconds.
✅ **Learning Tool** – Enhance LLMs with real, up-to-date information.

---

## 📌 Future Improvements

* [ ] Add support for **Bing Search API** (Azure Cognitive Search).
* [ ] Implement **caching** to reduce API calls.
* [ ] Add **streaming responses** for faster answers.
* [ ] Web/CLI interface for interactive use.

---

## 🎯 Why Use This?

Traditional LLMs **hallucinate** because they lack real-time knowledge.
This agent **grounds answers in real search results**, providing **reliable and cited answers**.

---

👉 Would you like me to also add a **demo Jupyter notebook** (`search_demo.ipynb`) so users can test queries interactively in Colab/Jupyter?

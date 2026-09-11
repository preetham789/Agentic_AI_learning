# Agentic AI

An educational Python workspace for learning modern agentic AI development with
LangChain, LangGraph, Model Context Protocol (MCP), retrieval-augmented
generation (RAG), evaluation, guardrails, structured outputs, tool use, and
multi-provider LLM routing.

The repository is organized as a hands-on notebook curriculum plus a few small
runnable Python examples. It is useful if you want to understand how individual
agent building blocks work before combining them into larger production-style
systems.

## Table of Contents

- [Project Goals](#project-goals)
- [What Is Inside](#what-is-inside)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Environment Variables](#environment-variables)
- [Running the Examples](#running-the-examples)
- [Learning Path](#learning-path)
- [RAG Data and Vector Stores](#rag-data-and-vector-stores)
- [MCP Demo Architecture](#mcp-demo-architecture)
- [Development Notes](#development-notes)
- [Troubleshooting](#troubleshooting)
- [Suggested Next Improvements](#suggested-next-improvements)

## Project Goals

This project is designed to help you learn how to:

- Connect to multiple LLM providers through LangChain and LiteLLM.
- Build basic and tool-using chatbots.
- Define tools and wire them into agents.
- Use LangChain message types and prompt patterns.
- Request structured model outputs with Pydantic, TypedDict, and dataclasses.
- Add middleware for summarization and human-in-the-loop workflows.
- Build LangGraph state machines for agent workflows.
- Expose tools through MCP servers and consume them from an agent.
- Ingest documents, split text, generate embeddings, persist vectors, retrieve
  relevant context, and generate RAG answers.
- Evaluate chatbot and RAG behavior with LangSmith-style workflows.

The code is intentionally notebook-heavy because the repository is primarily a
learning lab. You can run cells step by step, inspect intermediate objects, and
modify prompts, tools, models, retrievers, and vector stores as you learn.

## What Is Inside

The repository currently contains four major tracks:

| Track | Location | Focus |
| --- | --- | --- |
| LangChain basics | `langchain/` | Agents, model integrations, tools, messages, structured output, middleware, guardrails, evaluation, and LLM gateways. |
| LangGraph workflows | `langgraph/` | StateGraph basics, tool binding, graph invocation, checkpoints, and human-in-the-loop examples. |
| MCP examples | `MCP/` | Simple MCP math and weather servers plus a LangGraph/LangChain MCP client. |
| RAG pipeline | `RAG/` | Text/PDF loading, chunking, embeddings, ChromaDB vector storage, retrieval, and LLM answer generation. |

There is also a minimal installable package under `src/agentic_ai/` with the
console script `agentic-ai`. At the moment this package entry point is a small
placeholder, while the notebooks and MCP scripts contain the main learning
content.

## Tech Stack

Core tools and libraries used in this repository:

- Python 3.14, configured through `.python-version` and `pyproject.toml`.
- `uv` for dependency management and lockfile-based installs.
- LangChain for LLM integrations, agents, tools, messages, structured output,
  middleware, and retrievers.
- LangGraph for graph-based agent workflows.
- MCP Python SDK for exposing and consuming external tools.
- LiteLLM for LLM gateway patterns such as fallback chains, routing, caching,
  cost tracking, and load balancing.
- Groq, OpenAI, Google Gemini, Hugging Face, and Cohere integrations.
- Tavily search integration for tool-using graph examples.
- LangSmith for evaluation experiments.
- ChromaDB and Sentence Transformers for local vector search.
- PyPDF, PyMuPDF, and LangChain document loaders for document ingestion.
- Jupyter notebooks for interactive experimentation.

## Repository Structure

```text
Agentic_AI/
|-- README.md
|-- pyproject.toml
|-- uv.lock
|-- requirements.txt
|-- .python-version
|-- src/
|   `-- agentic_ai/
|       `-- __init__.py
|-- langchain/
|   |-- 1.langchainintro.ipynb
|   |-- 2.model_integration.ipynb
|   |-- 3.tools.ipynb
|   |-- 4.messages.ipynb
|   |-- 5.structuredoutput.ipynb
|   |-- 6.middelware.ipynb
|   |-- 7.guardrails.ipynb
|   |-- 8.rad_evaluation.ipynb
|   `-- 9.LLM_gateway.ipynb
|-- langgraph/
|   |-- 1-basicchatbot.ipynb
|   `-- 2-humanintheloop.ipynb
|-- MCP/
|   |-- mathserver.py
|   |-- weather.py
|   `-- client.py
`-- RAG/
    |-- notebook/
    |   |-- document.ipynb
    |   `-- pdf_loader.ipynb
    `-- data/
        |-- pdf/
        |-- text_files/
        `-- vector_store/
```

## Prerequisites

Install the following before running the examples:

- Python 3.14.
- `uv`.
- A notebook-capable editor such as VS Code, Cursor, JupyterLab, or Jupyter
  Notebook.
- API keys for whichever provider examples you want to run.

Check your local versions:

```powershell
python --version
uv --version
```

This project declares `requires-python = ">=3.14"`. If your system Python is
older, use `uv` to install and manage the required interpreter:

```powershell
uv python install 3.14
```

## Quick Start

From the repository root:

```powershell
cd C:\Users\preet\OneDrive\Desktop\Agentic_AI
uv sync
```

Activate the virtual environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or run commands through `uv` without activating:

```powershell
uv run python --version
uv run agentic-ai
```

If you prefer `pip`, this repository also includes `requirements.txt`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

`uv sync` is preferred because it uses `pyproject.toml` and `uv.lock`.

## Environment Variables

Create a `.env` file in the repository root. Only add the keys needed for the
notebooks or scripts you are running.

```env
# Main provider used across many notebooks and MCP client examples
GROQ_API_KEY=your_groq_api_key

# Optional provider integrations
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

# Search tool used by langgraph/1-basicchatbot.ipynb
TAVILY_API_KEY=your_tavily_api_key

# Evaluation notebooks
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
```

Do not commit real API keys. If you plan to publish or share the repository,
add `.env` and local vector-store artifacts to `.gitignore`.

## Running the Examples

### Run the Package Entry Point

The package currently exposes a minimal console command:

```powershell
uv run agentic-ai
```

Expected output:

```text
Hello from agentic-ai!
```

### Run Notebooks

The notebooks can be opened from VS Code, Cursor, JupyterLab, or classic
Jupyter. To register the environment as a Jupyter kernel:

```powershell
uv run python -m ipykernel install --user --name agentic-ai --display-name "Python (agentic-ai)"
```

Then open a notebook and select `Python (agentic-ai)` as the kernel.

If you want to launch JupyterLab without permanently adding it to the project:

```powershell
uv run --with jupyterlab jupyter lab
```

### Run the MCP Demo

The MCP example has:

- `MCP/mathserver.py`: local stdio MCP server with `add`, `sub`, `mul`, and
  `div` tools.
- `MCP/weather.py`: streamable HTTP MCP server with a simple `get_weather`
  tool.
- `MCP/client.py`: LangChain MCP client that collects tools from both servers
  and gives them to a LangGraph ReAct agent backed by Groq.

Start the weather server in one terminal:

```powershell
uv run python MCP\weather.py
```

Then run the client in a second terminal:

```powershell
uv run python MCP\client.py
```

The client starts the math server through stdio automatically and expects the
weather server to be reachable at:

```text
http://localhost:8000/mcp
```

Make sure `GROQ_API_KEY` is set in `.env` before running the MCP client.

## Learning Path

For the smoothest experience, run the notebooks in this order.

### 1. LangChain Foundations

Start with the `langchain/` notebooks.

| Notebook | Main ideas |
| --- | --- |
| `1.langchainintro.ipynb` | LangChain v1 introduction, Groq chat model usage, simple agent creation, and basic invocation. |
| `2.model_integration.ipynb` | Model initialization, OpenAI, Gemini, Groq, Hugging Face examples, invoke, stream, and batch patterns. |
| `3.tools.ipynb` | Tool decorators, binding tools to models, tool calls, and manual tool execution loops. |
| `4.messages.ipynb` | Human, system, and AI messages; prompt structure; role-specific context. |
| `5.structuredoutput.ipynb` | Structured output with Pydantic models, nested schemas, TypedDict, and dataclasses. |
| `6.middelware.ipynb` | Summarization middleware, thread IDs, human-in-the-loop middleware, approval and rejection flows. |
| `7.guardrails.ipynb` | Guardrail setup experiments and provider configuration. |
| `8.rad_evaluation.ipynb` | LangSmith client setup, LLM-as-judge metrics, evaluation runs, and RAG evaluation ideas. |
| `9.LLM_gateway.ipynb` | LiteLLM gateway concepts, fallbacks, cost tracking, caching, smart routing, load balancing, and LangChain integration. |

Note: `6.middelware.ipynb` and `8.rad_evaluation.ipynb` keep their current
filenames for compatibility with the existing repository, even though the words
are likely intended to be `middleware` and `rag_evaluation`.

### 2. LangGraph Workflows

After the LangChain basics, move to `langgraph/`.

| Notebook | Main ideas |
| --- | --- |
| `1-basicchatbot.ipynb` | State schema, `StateGraph`, START/END edges, Gemini chat model, Tavily tool binding, graph compilation, and graph invocation. |
| `2-humanintheloop.ipynb` | Checkpointing with `MemorySaver`, interrupt/resume workflows, human assistance tools, and middleware-style approval patterns. |

These notebooks introduce the mental model for agent workflows as graphs:
state enters a graph, nodes transform state, edges route execution, and
checkpointers preserve progress across turns.

### 3. MCP Tooling

The `MCP/` folder demonstrates how an agent can use tools exposed outside the
agent process.

The math server is a local stdio server:

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b
```

The weather server is a streamable HTTP server:

```python
@mcp.tool()
async def get_weather(location: str) -> str:
    return f"The weather in {location} is sunny."
```

The client uses `MultiServerMCPClient` to connect to both servers, fetch their
tools, and pass them into a LangGraph ReAct agent:

```python
tools = await client.get_tools()
agent = create_react_agent(model, tools)
```

### 4. RAG Pipeline

The `RAG/` notebooks build a local retrieval-augmented generation workflow.

| Notebook | Main ideas |
| --- | --- |
| `RAG/notebook/document.ipynb` | LangChain `Document` objects, text loading, directory loading, sample text files, and PDF loading. |
| `RAG/notebook/pdf_loader.ipynb` | PDF ingestion, chunking, Sentence Transformer embeddings, ChromaDB persistence, query retrieval, Groq-based answer generation, simple RAG, advanced RAG, confidence scoring, citations, and context handling. |

The advanced RAG notebook moves through the full pipeline:

1. Load PDF files from `RAG/data/pdf/`.
2. Split documents into overlapping chunks.
3. Generate embeddings with Sentence Transformers.
4. Store vectors in ChromaDB.
5. Retrieve relevant chunks for a query.
6. Send retrieved context to an LLM.
7. Return answers with optional context, citations, confidence, or streaming.

## RAG Data and Vector Stores

The repository includes sample local data:

```text
RAG/data/pdf/
RAG/data/text_files/
RAG/data/vector_store/
```

The PDF directory contains interview-prep, Docker, finance RAG, and AI/ML
reference material used by the RAG notebooks. The text directory contains small
plain-text examples such as Python and machine learning introductions.

The vector store directory contains ChromaDB artifacts. If you change the
embedding model, chunk size, chunk overlap, or source documents, regenerate the
vector store so retrieval results match the current data.

For large projects, treat vector stores as generated artifacts instead of source
code. A common production setup is:

- Keep source documents in durable storage.
- Store ingestion configuration in version control.
- Regenerate or migrate vector stores through repeatable scripts.
- Avoid committing large binary index files unless the project intentionally
  needs a portable demo dataset.

## MCP Demo Architecture

The MCP demo follows this flow:

```text
User question
   |
   v
LangGraph ReAct agent in MCP/client.py
   |
   v
MultiServerMCPClient
   |
   |-- stdio --> MCP/mathserver.py --> add/sub/mul/div
   |
   `-- HTTP  --> MCP/weather.py    --> get_weather
```

This pattern is useful because MCP lets you expose external capabilities as
tools without hard-wiring every tool directly into the agent process.

In this repository, the tools are intentionally simple. In a production system,
similar MCP servers could wrap:

- Internal APIs.
- Databases.
- Search services.
- File systems.
- Business workflow tools.
- Cloud services.
- Domain-specific calculators.

## Development Notes

### Dependency Management

Primary dependency files:

- `pyproject.toml`: project metadata, Python requirement, dependencies, and the
  `agentic-ai` console script.
- `uv.lock`: locked dependency graph used by `uv sync`.
- `requirements.txt`: pip-compatible dependency list.

Prefer:

```powershell
uv sync
```

Use `requirements.txt` only when working in an environment where `uv` is not
available.

### Package Entry Point

The current Python package is minimal:

```text
src/agentic_ai/__init__.py
```

It defines:

```python
def main() -> None:
    print("Hello from agentic-ai!")
```

This is a good place to later add reusable command-line workflows, such as:

- Running a RAG query from the terminal.
- Starting local MCP servers.
- Launching an agent demo.
- Rebuilding a vector store.
- Running an evaluation set.

### Recommended Notebook Practices

When experimenting in the notebooks:

- Run setup cells first so `.env` variables are loaded.
- Restart the kernel if model clients, vector stores, or tool bindings behave
  unexpectedly after edits.
- Keep provider-specific examples separated so missing optional API keys do not
  block unrelated lessons.
- Record important prompts, model names, chunk sizes, and retrieval settings in
  markdown cells next to the experiment.
- Clear large notebook outputs before committing to keep diffs readable.

### Security Notes

- Never commit `.env` files with real API keys.
- Be careful when running notebooks that call paid model APIs.
- Review tool definitions before connecting them to agents.
- Validate and sanitize inputs before exposing MCP servers beyond localhost.
- Add authentication and authorization before turning demo tools into networked
  services.
- Treat generated model output as untrusted unless verified.

## Troubleshooting

### `uv sync` Fails Because Python 3.14 Is Missing

Install Python 3.14 through `uv`:

```powershell
uv python install 3.14
uv sync
```

### Notebook Kernel Does Not See Dependencies

Register the virtual environment as a notebook kernel:

```powershell
uv run python -m ipykernel install --user --name agentic-ai --display-name "Python (agentic-ai)"
```

Then switch the notebook kernel to `Python (agentic-ai)`.

### Provider Authentication Errors

Check that the correct key exists in `.env` and that the notebook or script
loads it with `load_dotenv()`.

Common keys used by this repository:

- `GROQ_API_KEY`
- `OPENAI_API_KEY`
- `GOOGLE_API_KEY`
- `HUGGINGFACEHUB_API_TOKEN`
- `TAVILY_API_KEY`
- `LANGSMITH_API_KEY`

### MCP Client Cannot Connect to Weather Server

Start the weather server first:

```powershell
uv run python MCP\weather.py
```

Then run the client:

```powershell
uv run python MCP\client.py
```

The client expects:

```text
http://localhost:8000/mcp
```

If the server uses a different port or path, update the `weather` entry in
`MCP/client.py`.

### ChromaDB or Vector Store Errors

Try regenerating the vector store from the ingestion notebook when:

- Source documents changed.
- The embedding model changed.
- Chunk size or overlap changed.
- ChromaDB versions changed.
- Persisted files were moved between machines.

### Model Output Is Different Between Runs

LLM results can vary because of:

- Model version changes.
- Sampling settings.
- Provider-side updates.
- Different retrieved context.
- Changed prompts or message history.

For more reproducible experiments, record model names, prompts, temperature,
retriever settings, and dataset versions.

### Windows Path Issues

Because this repository lives under OneDrive, paths may contain spaces or be
synced while files are open. If you see path-related errors:

- Run commands from the repository root.
- Wrap paths in quotes when needed.
- Avoid moving vector stores while notebooks are running.
- Close notebooks before deleting or regenerating ChromaDB files.

## Suggested Next Improvements

This repository is already useful as a learning lab. The next upgrades that
would make it easier to reuse and share are:

- Add `.env.example` with placeholder keys.
- Add `.gitignore` for `.env`, notebook checkpoints, cache directories, and
  generated vector-store artifacts.
- Convert repeated notebook code into reusable modules under `src/agentic_ai/`.
- Add scripts for rebuilding the RAG vector store and running RAG queries.
- Add a CLI command for starting MCP demos.
- Add a small test suite for pure functions and tool behavior.
- Add formatting and linting configuration.
- Rename typoed notebook files when compatibility is not a concern.
- Add a license file if the project will be shared publicly.

## Current Status

The repository is best understood as an active educational workspace. The main
content is in notebooks and demo scripts, while the installable package is still
minimal. Use it to learn concepts, prototype workflows, and extract stable code
into `src/agentic_ai/` as patterns become clear.

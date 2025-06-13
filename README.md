# 🧪 Foundry Local Demo with Bot Framework & LangChain

Demo showcasing local AI using Azure Foundry Local, LangChain, OpenAI-compatible APIs, and Microsoft Bot Framework (Python).

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)

   * Run locally
   * Bot interaction
   * LangChain integration
6. [Project Structure](#project-structure)
7. [How It Works](#how-it-works)
8. [References](#references)

---

## 1. Overview

This project combines:

* **Microsoft Bot Framework (Python)** – handles chat interface.
* **Azure Foundry Local** – runs LLMs on-device via OpenAI-compatible endpoint [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/).
* **LangChain** – chains prompt templates with local LLM .
* **OpenAI-style API** – uses `openai` Python SDK to instruct Foundry local [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/).

---

## 2. Prerequisites

Ensure the following are installed:

* Python 3.10+
* [Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/how-to/how-to-use-langchain-with-foundry-local?pivots=programming-language-python) installed (Windows/macOS)
* Bot Framework SDK for Python
* `pip`–managed virtual environment (recommended: `venv` or `conda`)

---

## 3. Installation

```bash
# Clone the repo
git clone https://github.com/MusaddiqueHussainLabs/foundry_local_demo.git
cd foundry_local_demo

# Create virtual env
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows

# Install required packages
pip install -r requirements.txt
pip install foundry-local-sdk langchain[openai] botbuilder-integration-aiohttp
```

---

## 4. Configuration

Set up environment variables for Foundry Local:

```bash
export FOUNDRY_ALIAS="phi-3-mini-4k"
export BOT_APP_ID=""
export BOT_APP_PASSWORD=""
```

* `FOUNDRY_ALIAS`: Foundry model alias. Tip: list models via `foundry model list` [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/).
* Bot credentials: required for Microsoft Bot Framework.

---

## 5. Usage

### a) Run Foundry Local

```bash
foundry model run $FOUNDRY_ALIAS
```

This starts a local server, downloads a hardware-optimized model.

### b) Run the Bot Server

```bash
python app.py
```

Starts a bot endpoint (e.g., at `http://localhost:3978/api/messages`).

### c) Interact with the Bot

Use Bot Framework Emulator or integrate in Teams. Type in natural-language prompts and receive responses via Foundry + LangChain.

---

## 6. Project Structure

```
.
├── app.py              # Bot server + message routing
├── bot.py              # LangChain setup (prompt → LLM → response)
├── config.py           # configurations
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 7. How It Works

1. **Foundry Local**

   * Starts locally via `FoundryLocalManager`, loads a model alias [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/).
   * Exposes OpenAI-compatible endpoint at `http://localhost:<port>/`.

2. **LangChain Integration**

   * `ChatPromptTemplate` → `ChatOpenAI(llm=foundry endpoint)` [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/).

3. **Bot Framework Integration**

   * `app.py` routes messages: user input → LangChain chain → LLM → response back to user.

4. **OpenAI SDK usage**

   * Supports OpenAI-style calls (`openai.chat.completions.create`) for compatibility [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/).

---

## 8. References

* **Foundry Local overview & CLI Quickstart** [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/)

# Chula Student Assistant AI — Local AI

An AI chatbot for Chulalongkorn University information that runs **locally** with Ollama and Qwen 2.5 (3B). No Gemini API or cloud inference is used.

## Features
- Questions about transport, libraries, buildings, clubs and student services
- Uses the local `chula_knowledge.txt` knowledge base (41 curated Q&A records)
- Can answer Thai and English questions (quality varies)
- Interactive notebook-based chatbot

## How to run
1. Install [Ollama](https://ollama.com/download) on your computer.
2. Open Terminal and run `ollama pull qwen2.5:3b`.
3. Make sure Ollama is running (if needed, run `ollama serve`).
4. Download or clone this GitHub repository.
5. Open `Chula_Student_Assistant_AI.ipynb` in **local Jupyter Notebook or VS Code**, not hosted Google Colab.
6. Put `chula_knowledge.txt` in the notebook's current working directory.
7. Run the notebook's code cell. Ask questions and type `exit` to stop.

The chatbot connects to Ollama on `http://127.0.0.1:11434` on the **same computer**. No Gemini API key is needed. Internet is needed to install Ollama and download the model initially, but not for local inference.

## Files
- `Chula_Student_Assistant_AI.ipynb` — local AI chatbot
- `chula_knowledge.txt` — text knowledge base used for responses
- `chula_knowledge.csv` — structured Q&A records
- `sources.txt` — source references
- `requirements.txt` — dependency notes

## Example questions
- What is CU POP BUS?
- Where is the Central Library?
- จุฬาฯ มีรถรับส่งฟรีไหม?

## Limitations
- Prototype only; no real-time university updates.
- AI responses can be wrong. Check important information against official sources.
- Local model performance depends on your computer's memory and processing power.
- End-to-end inference has not yet been tested on the user's own computer.

Repository: https://github.com/Tichaya07/lnwAI

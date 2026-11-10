"""Chula Student Assistant AI - runs on a local model via Ollama.

Usage:  python chatbot.py
"""
import requests

# ===== SETTINGS =====
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:3b"      # any model you have pulled in Ollama, e.g. "llama3.2", "gemma2:2b"
KNOWLEDGE_FILE = "chula_knowledge.txt"

# Load Chula knowledge base (kept on your own computer)
with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
    knowledge = file.read()

SYSTEM_PROMPT = f"""
You are Chula Student Assistant AI.

Your job is to help Chulalongkorn University
students find information about campus life.

Use the knowledge base below to answer.

RULES:
1. Answer clearly and naturally.
2. Use only verified information from the knowledge base.
3. Never invent facts.
4. If information is unavailable, say so.
5. Respond in the same language as the student.
6. Keep answers concise and helpful.

KNOWLEDGE BASE:
{knowledge}
"""


def check_local_ai():
    """Make sure Ollama is running and the model is downloaded."""
    try:
        tags = requests.get("http://localhost:11434/api/tags", timeout=5).json()
    except requests.exceptions.ConnectionError:
        raise SystemExit("Ollama is not running. Install it from https://ollama.com and start it first.")
    names = [m["name"] for m in tags.get("models", [])]
    if not any(n == MODEL or n.startswith(MODEL + ":") for n in names):
        raise SystemExit(f"Model '{MODEL}' not found. Run:  ollama pull {MODEL}")


def ask_chula_ai(question):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            "stream": False,
            "options": {"temperature": 0.2, "num_ctx": 8192},
        },
        timeout=300,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]


if __name__ == "__main__":
    check_local_ai()
    print("Local AI connected! Model:", MODEL)
    print("Knowledge base loaded! Characters:", len(knowledge))

    print("================================")
    print("CHULA STUDENT ASSISTANT AI (Local AI)")
    print("Model:", MODEL)
    print("Type 'exit' to stop chatting")
    print("================================")

    while True:

        question = input("\nYou: ").strip()

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            answer = ask_chula_ai(question)
            print("\nChula AI:", answer)

        except Exception as e:
            print("\nError:", e)

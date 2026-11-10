# Chula Student Assistant AI

A local AI chatbot that helps Chulalongkorn University students easily access information about campus life, university facilities, transportation, student activities, and academic resources.

## Project Overview

Chula Student Assistant AI runs on a local AI model through [Ollama](https://ollama.com) on the user's own computer, together with a curated knowledge base, to answer students' questions about Chulalongkorn University. It does not need an internet-based AI service or an API key.

The chatbot aims to make campus information more accessible, especially for new and international students.

## Problem

University information is spread across many websites, social media pages, and university platforms. This makes it hard and slow for students to find what they need, especially freshmen and international students.

## Objectives

- Give students one convenient place to get university information.
- Reduce the time spent searching across multiple sources.
- Help new and international students get familiar with campus life.
- Build a local AI chatbot that gives clear, relevant answers from a university knowledge base.
- Show that a locally run AI can work without a cloud AI service, keeping student questions private and avoiding API costs.

## Expected Outcome

A working local AI chatbot prototype that answers common questions about Chulalongkorn University using a structured knowledge base, running entirely on a local machine. The project shows how locally hosted AI can improve the student experience in a private, low-cost, and offline-capable way.

## Features

- Question answering with a local AI model (default: `qwen2.5:3b`)
- Supports English and Thai questions
- Provides information about campus buildings and facilities
- Answers questions about CU POP BUS and transportation
- Provides information about libraries, student clubs, and activities
- Uses a knowledge base containing 41 curated Q&A records
- Avoids generating unsupported information when verified data is unavailable
- Runs offline after the model is downloaded; no API key needed

## Technologies Used

- Python
- Ollama (local AI runtime)
- Qwen 2.5 3B (local language model; can be swapped for another Ollama model)
- Jupyter Notebook
- TXT and CSV knowledge base

## Project Files

| File | Description |
|---|---|
| Chula_Student_Assistant_AI.ipynb | Main chatbot code (notebook) |
| chatbot.py | Same chatbot as a plain Python script |
| chula_knowledge.txt | Knowledge base used by the chatbot |
| chula_knowledge.csv | Structured Q&A dataset |
| sources.txt | References and official university sources |
| requirements.txt | Python dependencies |
| README.md | Project documentation |

## How to Run

1. Install Ollama from https://ollama.com and open it.
2. Download the model in a terminal:
   ```
   ollama pull qwen2.5:3b
   ```
3. Install the Python dependency:
   ```
   pip install -r requirements.txt
   ```
4. Run the chatbot, either:
   - `python chatbot.py`, or
   - open `Chula_Student_Assistant_AI.ipynb` in Jupyter / VS Code and run all cells.
5. Enter questions to chat. Type `exit` to stop.

Keep `chula_knowledge.txt` in the same folder as the code. To use a different model, change `MODEL` in the code (for example `llama3.2` or `gemma2:2b`) and `ollama pull` it first.

## Example Questions

- Where is Chulalongkorn University located?
- What is CU POP BUS?
- What services does the Central Library offer?
- What student clubs are available?
- Where can I find information about student activities?

## Knowledge Base

The knowledge base contains 41 curated question-and-answer records covering campus information, transportation, libraries, clubs, activities, buildings, and university services. It is stored locally in TXT and CSV formats, with links to official university sources.

Information was compiled from publicly accessible university resources. Some details, such as operating hours and club activities, may change over time.

## Limitations

- The chatbot only uses information available in its knowledge base.
- It does not provide real-time university updates.
- Some information may require verification through official university websites.
- Small local models may answer less accurately than large cloud models, especially in Thai.
- Response speed depends on the user's computer hardware.
- The current prototype runs in a terminal or notebook rather than a standalone website.

## Future Improvements

- Develop a user-friendly web interface.
- Expand the knowledge base with more university information.
- Add retrieval (search over the knowledge base) so it scales to more records.
- Add campus maps and navigation features.
- Integrate real-time university announcements.

## GitHub Repository

https://github.com/Tichaya07/lnwAI

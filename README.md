# Chula Student Assistant AI

An AI-powered chatbot designed to help Chulalongkorn University students easily access information about campus life, university facilities, transportation, student activities, and academic resources.

## Project Overview

Chula Student Assistant AI uses Google's Gemini API and a curated knowledge base to answer students' questions about Chulalongkorn University.

The chatbot aims to make campus information more accessible, especially for new and international students.

## Features

- AI-powered question answering using Gemini
- Supports English and Thai questions
- Provides information about campus buildings and facilities
- Answers questions about CU POP BUS and transportation
- Provides information about libraries, student clubs, and activities
- Uses a knowledge base containing 41 curated Q&A records
- Avoids generating unsupported information when verified data is unavailable

## Technologies Used

- Python
- Google Colab
- Google Gemini API
- Google GenAI Python SDK
- TXT and CSV knowledge base

## Project Files

| File | Description |
|---|---|
| Chula_Student_Assistant_AI.ipynb | Main chatbot code |
| chula_knowledge.txt | Knowledge base used by the chatbot |
| chula_knowledge.csv | Structured Q&A dataset |
| sources.txt | References and official university sources |
| requirements.txt | Python dependencies |
| README.md | Project documentation |

## How to Run

1. Open `Chula_Student_Assistant_AI.ipynb` in Google Colab.
2. Upload `chula_knowledge.txt` to the Colab Files panel.
3. Create a Gemini API key through Google AI Studio.
4. Open Colab Secrets and add the key under `GEMINI_API_KEY`.
5. Enable Notebook access for the secret.
6. Run all code cells in order.
7. Enter questions to interact with the chatbot.
8. Type `exit` to stop the chatbot.

**Note:** A personal Gemini API key is required. API keys are not included in this repository.

## Example Questions

- Where is Chulalongkorn University located?
- What is CU POP BUS?
- What services does the Central Library offer?
- What student clubs are available?
- Where can I find information about student activities?

## Knowledge Base

The knowledge base contains 41 curated question-and-answer records covering campus information, transportation, libraries, clubs, activities, buildings, and university services.

Information was compiled from publicly accessible university resources. Some details, such as operating hours and club activities, may change over time.

## Limitations

- The chatbot only uses information available in its knowledge base.
- It does not provide real-time university updates.
- Some information may require verification through official university websites.
- The current prototype runs in Google Colab rather than a standalone website.

## Future Improvements

- Develop a user-friendly web interface.
- Expand the knowledge base with more university information.
- Add campus maps and navigation features.
- Integrate real-time university announcements.
- Improve search accuracy and information retrieval.

## GitHub Repository

https://github.com/Tichaya07/lnwAI

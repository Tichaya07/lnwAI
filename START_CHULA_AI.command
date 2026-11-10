#!/bin/bash
set -e
cd "$(dirname "$0")"
printf "\n=== Chula Student Assistant AI — Mac ===\n"
if ! command -v python3 >/dev/null 2>&1; then
 echo "Python 3 is required. Install it from https://www.python.org/downloads/macos/"
 read -r -p "Press Enter to close..."; exit 1
fi
if ! command -v ollama >/dev/null 2>&1; then
 if [ -x /Applications/Ollama.app/Contents/Resources/ollama ]; then
   export PATH="/Applications/Ollama.app/Contents/Resources:$PATH"
 else
   echo "Please install Ollama from https://ollama.com/download, open it once, then rerun this file."
   open "https://ollama.com/download"
   read -r -p "Press Enter to close..."; exit 1
 fi
fi
open -a Ollama >/dev/null 2>&1 || true
if [ ! -f chula_knowledge.txt ]; then
 echo "Downloading Chula knowledge base from the project GitHub..."
 curl --fail --location --silent --show-error --retry 2 --output chula_knowledge.txt \
   'https://raw.githubusercontent.com/Tichaya07/lnwAI/main/chula_knowledge.txt' || {
   echo "Download failed. Save chula_knowledge.txt from GitHub beside this script and retry."
   read -r -p "Press Enter to close..."; exit 1;
 }
fi
echo "Checking Ollama server..."
for i in 1 2 3 4 5 6 7 8 9 10; do
 if curl --silent --fail http://127.0.0.1:11434/api/tags >/dev/null; then break; fi
 sleep 2
done
if ! curl --silent --fail http://127.0.0.1:11434/api/tags >/dev/null; then
 echo "Ollama is not running. Open the Ollama app and try again."
 read -r -p "Press Enter to close..."; exit 1
fi
echo "Checking/downloading local Qwen model (first run may take several minutes)..."
ollama pull qwen2.5:3b
printf "\nStarting chat...\n"
python3 chula_chat.py
read -r -p "Press Enter to close..."

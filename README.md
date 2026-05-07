## Setup
 
1. Create and activate a virtual environment
2. Install dependencies (added later)
3. Run scripts in the `scripts/` folder
 
## Run
 
```bash
python scripts/hello_ai.py
---
 

# CLI Assistant

This is a simple Python command-line AI assistant.

It takes a user prompt and gives a response using the OpenRouter API.

## Requirements

- Python
- OpenRouter API key

## Setup

1. Create a virtual environment:
   ```powershell
   python -m venv .venv
   ```

2. Activate it:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install packages:
   ```powershell
   pip install requests python-dotenv
   ```

4. Create a `.env` file and add your API key:
   ```env
   OPENROUTER_API_KEY=your_api_key_here
   ```

## Run

```powershell
python .\scripts\cli_assistant.py
```

## Example

Input:
```text
Explain AI in one simple sentence.
```

Output:
```text
AI is technology that helps computers understand and respond to information.
```

## Note

Do not upload your `.env` file to GitHub.

##  Initialize Git locally
```bash
git init
git add .
git commit -m "Day 2: initial project setup"
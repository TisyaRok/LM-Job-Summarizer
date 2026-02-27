LM Job Summarizer

A Python-based utility that uses the Google Gemini 2.5 Flash API to parse lengthy job descriptions and extract the top 5 must-have skills. This project demonstrates LLM integration, secure API key management, and automated text processing.

## Features
- **Precise Extraction:** Uses prompt engineering to constrain output to exactly 5 key skills.
- **Secure Configuration:** Implements `.env` patterns to keep API keys out of version control.
- **Cross-Platform:** Works on Windows, macOS, and Linux.

## Tech Stack
- **Language:** Python 3.10+
- **AI Model:** Google Gemini 2.5 Flash
- **Libraries:** `google-genai`, `python-dotenv`

## Getting Started

### 1. Prerequisites
Ensure you have Python installed. Then, install the required dependencies:
```bash
pip install google-genai python-dotenv
2. API Setup
Get a free API key from Google AI Studio.

In the root directory of this project, create a file named .env.

Add your key to the file:

Plaintext
GEMINI_API_KEY=your_actual_api_key_here
3. Usage
Paste your target job description into job_description.txt.

Run the summarizer:

Bash
python summarize_job.py
📂 Project Structure
summarize_job.py: The core logic for calling the Gemini API.

job_description.txt: The input file for the job text.

.env: (Hidden) Stores your private API keys.

.gitignore: Ensures sensitive files like .env are not uploaded to GitHub.

Lessons Learned
Security: Successfully implemented python-dotenv after a credential leak to practice industry-standard secret management.

API Versioning: Adapted code to handle the 2026 transition from Gemini 2.0 to 2.5 model endpoints.

Prompting: Developed specific system instructions to ensure consistent output formatting.

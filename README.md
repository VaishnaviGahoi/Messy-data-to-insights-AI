🚀 AI Data Architect: Raw Data to Insights
Built for the Google "Build the Future" Showcase

💡 The Problem
Small business owners often manage data through messy handwritten notes, inconsistent logs, or unstructured text. As an aspiring Data Analyst, I realized that the biggest barrier to meaningful analysis is the time spent on manual data cleaning and entry.

🛠️ The Solution
This prototype uses Gemini 1.5 Flash to act as an automated "Data Architect." It extracts critical entities—Date, Description, Category, and Amount—from any raw text input and organizes them into a structured Markdown table ready for SQL databases or Excel.

✨ Key Features
Intelligent Extraction: Processes natural language (e.g., "Paid 4k for 50kg steel on Dec 24") into structured columns.

Persona-Driven AI: Uses specific System Instructions to maintain a professional "Senior Data Architect" voice.

Secure API Handling: Built with Streamlit Secrets to prevent API key exposure.

🏗️ Technical Stack
Language: Python.

AI Model: Google Gemini 1.5 Flash.

Framework: Streamlit (for the interactive UI and deployment).

Data Handling: Pandas.

🚀 Getting Started
Clone the repo: git clone https://github.com/yourusername/ai-data-architect.git.

Install dependencies: pip install -r requirements.txt.

Setup API Key: Add your GEMINI_API_KEY to .streamlit/secrets.toml.

Run the app: streamlit run app.py.
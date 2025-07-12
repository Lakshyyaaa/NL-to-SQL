## Ask Your Database (Natural Language to SQL)
Upload any SQLite database and ask natural language questions.
Streamlit + Gemini auto-generates SQL queries and displays results instantly.

## Features
1.Upload .db (SQLite) files directly in the UI
2.Ask questions like: "List all employees older than 30"
3.Generates SQL queries using Gemini 2.5
4.Executes and displays results live
5.Clean Streamlit UI with syntax-highlighted SQL

## Tech Stack
Frontend & Backend: Streamlit
LLM: Google Gemini (via google-generativeai)
Database: SQLite

### Running the Repository locally

Copy
git clone https://github.com/your-username/nl-to-sql-streamlit.git
cd nl-to-sql-streamlit

Install dependencies:
pip install streamlit google-generativeai

Set your Gemini API key in app.py:
genai.configure(api_key="your-api-key")

Run the Streamlit app:
streamlit run app.py

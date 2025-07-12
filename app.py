
import streamlit as st
import sqlite3
import google.generativeai as genai

key = 'Your Key'
genai.configure(api_key=key)

def extract_schema(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    schema = ""
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    for table in tables:
        table_name = table[0]
        cur.execute(f"PRAGMA table_info({table_name});")
        columns = cur.fetchall()
        col_names = [col[1] for col in columns]
        schema += f"Table: {table_name} | Columns: {', '.join(col_names)}\n"

    conn.close()
    return schema.strip()

def get_response(question, schema):
    prompt = f"""
    You are an expert in converting natural language questions to SQL queries.

    Here is the schema of the SQLite database:
    {schema}

    Based on this schema, write a valid SQL query for the following question:
    {question}

    Return only the SQL query. Do not explain anything. No markdown.
    """

    model = genai.GenerativeModel('models/gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text.strip()

def read_sql(sql, db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

st.set_page_config(page_title="Ask Your Database with Gemini")
st.header("Upload any SQLite Database and Ask Questions")

question = st.text_input("Enter your question:")
uploaded_file = st.file_uploader("Upload a SQLite (.db) file", type=["db"])
submit = st.button("Ask")

if submit and uploaded_file:
    with open("temp.db", "wb") as f:
        f.write(uploaded_file.read())

    sql = get_response(question, extract_schema("temp.db"))
    st.code(sql, language="sql")

    rows = read_sql(sql, "temp.db")
    st.subheader("Query Results:")
    [st.write(r) for r in rows] if rows else st.info("No results found.")



import streamlit as st
import os
import sqlite3
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key="AIzaSyCin2PxUcVVcsCDc8K3SWlyOHaCy4JIFVY")


def get_gemini_response(question,prompt):
    model= genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question]) # behavior of the model
    return response.text


def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

response = "SELECT * FROM STUDENT WHERE CLASS='Data Science'"
data = read_sql_query(response, "student.db")
    

#define the prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present. the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \n Example 2- Tell me all the students studying in Data Science class?, The SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";
    also the sql code should not have ``` in beginning or end ad sql word in output
    """
]

st.set_page_config(page_title="LLM Based SQL APP")
st.header("Gemini app to retrieve SQL data")
st.header("Enter your text")
question = st.text_input("input: ",key="input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(data)
        st.header(data)

from openai import OpenAI
import streamlit as st

f = open(r"C:\Users\farheen\OneDrive\Desktop\internship_24\genai_app\genai_app_1\.open_ai_key.txt")
OPENAI_API_KEY = f.read()

st.title("🔎AI Code Reviewer")

client = OpenAI(api_key = OPENAI_API_KEY)

prompt = st.text_input("Enter your python code here....")

if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an Expert in code review. So, find bugs, errors and give the corrected code."},
        {"role": "user", "content": prompt}
      ]
    )
    st.write(response.choices[0].message.content)
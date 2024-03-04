import os
import streamlit as st
import openai
from PyPDF2 import PdfReader
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY", None)

SYSTEM_MESSAGE = """
You are expert in answering user's questions based on given article.
"""

USER_MESSAGE = """
User's question: {question}

Article: {article}
"""

if not openai_api_key:
    st.error("Please add your OpenAI API key to continue.")

with st.sidebar:
    st.title("Some sidebar title")
    st.write("Some sidebar content")

st.title("📝 PDF Q&A with Openai & InsourceData")

uploaded_file = st.file_uploader("Upload a pdf, txt, or md", type=("txt", "md", "pdf"))

question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question and not openai_api_key:
    st.info("Please add your Anthropic API key to continue.")


if uploaded_file and question and openai_api_key:
    article_name = uploaded_file.name
    if article_name.endswith(".pdf"):
        pdf_reader = PdfReader(uploaded_file)
        article = " ".join(page.extract_text() for page in pdf_reader.pages)
    else:
        article = uploaded_file.read().decode("utf-8")

    messages = [
        {'role': 'system', 'content': SYSTEM_MESSAGE},
        {'role': 'user', 'content': USER_MESSAGE.format(question=question, article=article)}
    ]

    response  = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        temperature=0.0,
        max_tokens=300,
    )
    print(response)
    st.write("### Answer")
    st.write(response.choices[0].message.content)
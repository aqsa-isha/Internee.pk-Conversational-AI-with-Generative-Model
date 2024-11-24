from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit App Setup
st.set_page_config(page_title="Gemini Q&A Demo", page_icon="🤖", layout="wide")

# Sidebar
with st.sidebar:
    st.title("Gemini Q&A")
    st.markdown(
        """
        Welcome to the **Gemini Q&A App**!  
        Powered by **Gemini Pro LLM**, this application allows you to engage in real-time intelligent conversations.
        """,
        unsafe_allow_html=True,
    )
    if st.button("🗑 Clear Chat History"):
        st.session_state['chat_history'] = []

# Header Section
st.markdown(
    """
    <style>
        .header {
            font-size: 28px;
            font-weight: bold;
            color: #4B72E0;
            text-align: center;
            margin-bottom: 5px;
        }
        .sub-header {
            font-size: 16px;
            color: #555555;
            text-align: center;
            margin-bottom: 10px;
        }
        .prompt-container {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.1);
        }
        .response-container {
            background-color: #e9f5fb;
            padding: 10px;
            border-radius: 6px;
            margin: 5px 0;
        }
        .chat-user {
            background-color: #d1ffd6;
            padding: 10px;
            border-radius: 6px;
            margin: 5px 0;
        }
        .chat-bot {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 6px;
            margin: 5px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="header">Gemini LLM Application</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Ask questions and get intelligent responses powered by Gemini Pro</div>', unsafe_allow_html=True)

# Input Section
st.write("---")
st.markdown('<div class="prompt-container">', unsafe_allow_html=True)
st.markdown("### 💬 Ask a Question")
input = st.text_input("Enter your question:", key="input", help="Type your question here.")
submit = st.button("Ask", help="Click to submit your question")
st.markdown('</div>', unsafe_allow_html=True)

# Display Chat History and Responses
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if submit and input:
    with st.spinner("Processing..."):
        response = get_gemini_response(input)
        st.session_state['chat_history'].append(("You", input))
        bot_response = ""
        for chunk in response:
            bot_response += chunk.text
        st.session_state['chat_history'].append(("Bot", bot_response))

# AI Response Section
if submit and input:
    st.markdown("### 🧠 AI's Response:")
    st.markdown(
        f"<div class='response-container'><strong>Gemini:</strong> {bot_response}</div>",
        unsafe_allow_html=True,
    )

# Chat History Section
st.markdown("### 📜 Chat History")
with st.expander("Show/Hide Chat History", expanded=True):
    for role, text in st.session_state['chat_history']:
        role_class = "chat-user" if role == "You" else "chat-bot"
        st.markdown(
            f"<div class='{role_class}'><strong>{role}:</strong> {text}</div>",
            unsafe_allow_html=True,
        )

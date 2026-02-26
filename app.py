import streamlit as st
from dotenv import load_dotenv
import os

from gemini_service import GeminiService
from prompt_manager import PromptManager
from logger import setup_logger

load_dotenv()
setup_logger()

st.title("Career Advisor Chatbot")

if "gemini_service" not in st.session_state:
    st.session_state.gemini_service = GeminiService()

if "chat_session" not in st.session_state:
    system_prompt = PromptManager.get_system_prompt()
    st.session_state.chat_session = (
        st.session_state.gemini_service.create_chat(system_prompt)
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, text in st.session_state.messages:
    st.markdown(f"**{role.capitalize()}:** {text}")

user_input = st.chat_input("Ask about career advices...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.spinner("Thinking..."):
        reply = st.session_state.gemini_service.send_message(
            st.session_state.chat_session,
            user_input
        )

    st.session_state.messages.append(("bot", reply))
    st.rerun()
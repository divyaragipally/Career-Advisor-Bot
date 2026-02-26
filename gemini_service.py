import os
from google import genai
import logging

class GeminiService:
    def __init__(self):
        self.client = genai.Client()

    def create_chat(self, system_prompt):
        try:
            chat_session = self.client.chats.create(
                model="gemini-2.5-flash",
                config=genai.types.GenerateContentConfig(
                    system_instruction=system_prompt,
                )
            )
            logging.info("Chat session created successfully")
            return chat_session
        except Exception as e:
            logging.error(f"Error creating chat session: {e}")
            raise

    def send_message(self, chat_session, message):
        try:
            response = chat_session.send_message(message)
            logging.info("Message sent successfully")
            return response.text
        except Exception as e:
            logging.error(f"Error sending message: {e}")
            return "Sorry, I am facing technical issues. Please try again."

import numpy as np
import chainlit as cl
import os
from dotenv import load_dotenv
import openai

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

CHAT_HISTORY = []

# pass Message into ChatGPT API .send() the answer



@cl.on_message
async def main(message: str):
    
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [{"role": "system" , "content": "You are a virtual travel planning assistant. Your name is Lucie. You help with anything travel related. Use Emojis and have a friendly and enthusiastic tone. Try to answer in a few sentences."},
                    {"role": "user", "content": message}], 
        temperature = 1,
    )
    print("message:", message)
    print("response:", response)
    
    await cl.Message(content=response["choices"][0]["message"]["content"]).send()
    
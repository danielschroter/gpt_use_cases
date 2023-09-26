
import numpy as np
import chainlit as cl
import os
from dotenv import load_dotenv
import openai

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


@cl.on_message
async def main(message: str):
    await cl.Message(content=message).send()
    
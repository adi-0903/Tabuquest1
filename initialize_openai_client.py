import os
import openai

def initialize_openai_client():
    # Initialize OpenAI client without 'proxies'
    client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))
    return client

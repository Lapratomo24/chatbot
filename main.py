from dotenv import load_dotenv
import os
import sys
import openai

load_dotenv()

def main():
    '''parse environment variable'''
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Missing API Key. Program aborted.")
        sys.exit(1)
    
    if len(sys.argv) < 2:
        print("Usage: Type in 'python chatbot.py <chatbot_name>'")
        sys.argv(1)
        
    chatbot_name = sys.argv[1]
    openai.api_key = api_key


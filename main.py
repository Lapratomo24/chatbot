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
        sys.exit(1)
        
    chatbot_name = sys.argv[1]
    openai.api_key = api_key

    chat = [
        {"role": "system", "content": f"You are a friendly assistant named {chatbot_name}."}
    ]
    
    total_tokens_used = 0
    
    print(f"Hello, I'm you friendly assistant {chatbot_name}. How can I assist you today?")
    print("(Press Ctrl+D to exit)")
    
    try:
        while True:
            try:
                user_input = input("You: ")
            
            except EOFError:
                print("\nBye!")
                print(f"Total tokens used: {total_tokens_used}.")
                break
            
            chat.append({"role": "user", "content": user_input})
            
            try:
                response = openai.ChatCompletion.create(
                    messages=chat,
                    model="gpt-3.5-turbo",
                )
                
                ai_message = response["choices"][0]["message"]["content"]
                total_tokens_used += response["usage"]["total_tokens"]
                print(f"{chatbot_name}: {ai_message}")
                
                chat.append({"role": "assistant", "content": ai_message})
            
            except openai.error.openAIError as e:
                print(f"Error: {e}")
                break
        
    except KeyboardInterrupt:
        print("\nBye!")
        print(f"Total tokens used: {total_tokens_used}.")
    

if __name__ == "__main__":
    main()


#step 1 

import openai 
import os
from dotenv import load_dotenv 

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

#step 2
def ask_chat_gpt(prompt, modelo= "text-davinci-002"):
    answer = openai.Completion.create(
        engine = modelo,
        prompt = prompt,
        n = 1,
        max_tokens = 150,
        #creatividad entre 0 - 1 entre mas bajo mas racional 
    
        temperature = 1.5 
    )

    return answer.choices [0]. text.strip()

#step  3 
print ( "Hi! Welcome to the chat. Type 'exit' to exit")

while True:
    intake_user = input ("\nYou:")
    if intake_user.lower == "exit":
        break

    prompt = f"User asks: {intake_user}\nChatGPT responde: "
    ask_gpt = ask_chat_gpt(prompt)
    print(f"Chatbot: {ask_gpt}")

fileopen = open("Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()

from dotenv import load_dotenv
import openai

openai.api_key = API

load_dotenv()
completion = openai.Completion()

chat_log_template = '''You : Hello, who are you?
Jarvis : I am doing great. How can I help you today?
'''

def Reply(question, chat_log=None):
    if chat_log is None:
        chat_log = chat_log_template
    prompt = f'{chat_log}You : {question}\nJarvis :'
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "How are you?"},
        ]
    )
    #answer = response.choices[0].text.strip()
    return response.choices[0].message.content

# Reply("how are you?")
print(Reply("how are you?"))
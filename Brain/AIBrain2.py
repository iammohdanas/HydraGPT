import openai
from dotenv import load_dotenv
#openai.api_key = "sk-xxxx"
fileopen = open("Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()
openai.api_key = API
load_dotenv()
completion = openai.Completion()



response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "How are you?"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)

#API Key
fileopen = open("Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv

#coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log=None):
    FileLog = open("Database\\chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nHydra : '
    # response = completion.create(
    #     model = "text-davinci-002",
    #     prompt=prompt,   
    #     temperature=0.5,
    #     max_tokens=60,
    #     top_p=0.3,
    #     frequency_penalty=0.5,
    #     presence_penalty=0)
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": question},
        ]
    )

    answer = response.choices[0].message.content
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nHydra : {answer}"
    FileLog = open("Database\\chat_log.txt","w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answer

# reply = ReplyBrain("Hello, I am Anas Ansari")
# print(reply)
while True:
    kk= input("Enter : ")
    print(ReplyBrain(kk))
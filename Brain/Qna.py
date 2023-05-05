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
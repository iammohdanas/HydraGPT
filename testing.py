# import os
# import json
# with open("Data\\keywords.json",'r') as f:
#         intents = json.load(f)
# for intent in intents['intents']:
#         tag = intent['tag']
#         print(intent['patterns'])

from Arms.heart import predictHeartDisease
predictHeartDisease()
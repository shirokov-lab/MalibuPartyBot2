import os
import json
TOKEN = os.getenv('TOKEN')
PAY_TOKEN = os.getenv('PAY_TOKEN')

TEXTS={}
with open('text/texta.json',encoding='utf8') as file:
    TEXTS=json.load(file)
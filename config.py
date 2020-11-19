import os
import json
TOKEN = os.getenv('TOKEN')
PAY_TOKEN = os.getenv('PAY_TOKEN')
ADMINS_ID = [454709994, 685001761, 693267094]

TEXTS={}
with open('text/texta.json',encoding='utf8') as file:
    TEXTS=json.load(file)
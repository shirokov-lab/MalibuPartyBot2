import os
import json
TOKEN = os.getenv('TOKEN')
PAY_TOKEN = os.getenv('PAY_TOKEN')
ADMINS_ID = [356987496, 454709994, 685001761]

TEXTS={}
with open('text/texta.json',encoding='utf8') as file:
    TEXTS=json.load(file)
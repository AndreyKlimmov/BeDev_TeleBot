# BeDev_EnglishWordMeaning
# @Be_Dev_English_Bot
# 5450847244:AAHMfh_VpngOG9t6LJWGNhBVwH1z21F1y_g
# https://api.telegram.org/bot5450847244:AAHMfh_VpngOG9t6LJWGNhBVwH1z21F1y_g/getUpdates
# https://api.telegram.org/bot5450847244:AAHMfh_VpngOG9t6LJWGNhBVwH1z21F1y_g/getUpdates?offset={update_id + 1}
# https://api.telegram.org/bot5450847244:AAHMfh_VpngOG9t6LJWGNhBVwH1z21F1y_g/sendMessage?'chat_id': chat_id, 'text': message_text

import requests

users = [{
    "id": 0,
    "level": 0,
    "name": "Anna"
    },
        {
    "id": 5370301083,
    "level": 2,
    "name": "Petr"
    }]

sentences = [
    {"text": "Most sentences contain a subject and a verb",
    "level": 0},
    {"text": "Data is one of the most critical assets of any business",
    "level": 1},
    {"text": "A sentence is a group of words which, when they are written down, begin with a capital letter and end with a full stop, question mark, or exclamation mark",
    "level": 1},
    {"text": "The high character which the corps has won is in itself a valuable asset",
    "level": 1},
    {"text": "I was taken into custody",
    "level": 2},
    {"text": "He took the book from the table",
    "level": 0}
]

TOKEN = '5450847244:AAHMfh_VpngOG9t6LJWGNhBVwH1z21F1y_g'

ROOT_URL = f'https://api.telegram.org/bot{TOKEN}'

def get_update(url, update_id):
    responce = requests.get(f'{url}/getUpdates?offset={update_id + 1}')
    return responce.json()

def send_message(chat_id, message_text, url):
    data = {'chat_id': chat_id, 'text': message_text}
    responce = requests.post(f'{url}/sendMessage', data = data)

answered_update_id = 0
update_id = 0

while True:
    message_text = ''
    output_sentences = []
    updates = get_update(ROOT_URL, answered_update_id)
    if updates.get('result'):
        update_id = updates.get('result')[0]['update_id']
        user_id = updates.get('result')[0]['message']['from']['id']
        for user in users:
            if user_id == user.get('id'):
                for i in sentences:
                    if i.get("level") == user.get('level'):
                        if updates.get('result')[0]['message']['text'] in i["text"]:
                            output_sentences.append(i["text"])

    if len(output_sentences) == 0:
        message_text = "Not found"
    else:
        for i in output_sentences:
            message_text = message_text + i + '\n'

    if update_id != answered_update_id:
        chat_id = updates.get('result')[0]['message']['chat']['id']
        send_message(chat_id, message_text, ROOT_URL)
        answered_update_id = update_id

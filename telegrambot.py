from flask import Flask, request, Response
import requests
import json


TOKEN = "5333018057:AAFaPBZyBc2-JvtCJGyMykrbllo18P9_cF8"

app = Flask(__name__)



def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(url, json=payload)
    return r


if __name__ == '__main__':
    appT
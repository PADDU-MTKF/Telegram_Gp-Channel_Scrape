import dotenv
from dotenv import load_dotenv
import os
load_dotenv()
dot_file=dotenv.find_dotenv()

API_ID   = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE    = os.getenv('PHONE')
CHAT     = os.getenv('CHAT')
API_KEY  = os.getenv('API_KEY')
CHAT_ID  = os.getenv('CHAT_ID')

def update_env(key,value):
    global dot_file
    dotenv.set_key(dot_file,key,str(value))

LINK='https://api.telegram.org/bot'+API_KEY+'/sendMessage'
LINK_MEDIA='https://api.telegram.org/bot'+API_KEY+'/sendPhoto'

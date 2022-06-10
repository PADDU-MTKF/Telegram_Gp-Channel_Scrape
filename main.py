import telethon
from telethon.sync import TelegramClient
import datetime
import time
import os
from config import *
import requests as req
from dotenv import load_dotenv

load_dotenv()



def send_error(er):
    if er=='login_code':
        print ("login error")

def get_code():
    code=input('Please enter code re :- ')
    return code

def connect(PHONE,API_ID, API_HASH):

    client = TelegramClient('you_r_great', API_ID, API_HASH)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(PHONE)
        try:
            code=get_code()
            client.sign_in(PHONE, code)
        except telethon.errors.rpcerrorlist.PHONECodeInvalidError :
            send_error('login_code')

    else:
        pass




connect(PHONE,API_ID, API_HASH)


try:
    file=open('last_update_id_host.txt','r')
    contt=file.read()
    update_id_host=int(contt)
    file.close()
except:
    update_id_host=0


def forward(text,old_file_list):
    new_file_list=os.listdir()
    fil_name=None
    for fil in new_file_list:
        if fil not in old_file_list and "you_r_great" not in fil:
            fil_name=fil
            break

    if fil_name is None:
        PARA={'chat_id':CHAT_ID,'text':text}
        req.post(LINK,data=PARA)
    else:
        PARA={'chat_id':CHAT_ID,'caption':text}
        f=open(fil_name,'rb')
        files={'photo':f}

        a=req.post(LINK_MEDIA,data=PARA,files=files)
        time.sleep(2)

        f.close()
        os.remove(fil_name)

    #print(text)

def save():
    global update_id_host,latest_id
    update_id_host=latest_id
    file=open('last_update_id_host.txt','w')
    file.write(str(update_id_host))
    file.close()
    file_list=os.listdir()
    client.download_media(message.media)
    forward(message.text,file_list)

while True:
    time.sleep(3)
    try:
        with TelegramClient('you_r_great', API_ID, API_HASH) as client:
            flag=0
            try:
                for message in client.iter_messages(CHAT, offset_date=datetime.date.today() ,offset_id=update_id_host, reverse=True):
                    time.sleep(1)
                    try:
                        latest_id=message.id
                        if update_id_host==0:
                            flag=1
                        elif update_id_host>=latest_id:
                            pass
                        else:
                            save()
                    except:
                        pass
                if flag==1:
                    save()
            except:
                pass
    except:
        pass

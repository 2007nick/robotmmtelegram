from telethon.sync import TelegramClient
from telethon import utils
import csv
from csv import reader
import configparser
import time





done = False
with open('phone.csv', 'r') as f:
    str_list = [row[0] for row in csv.reader(f)]

    
    po = 0
    for pphone in str_list:
        
        
        phone = utils.parse_phone(pphone)
        po += 1
        
        
        print(f"Login {phone}")
        client = TelegramClient(f"sessions/{phone}", 2075988, '0d736429473d31199be9e61dc6afa2cd')
        time.sleep(1)
        try:
         client.start(phone)
        except:
         print("erro de sessao")

        client.disconnect()
        print()
    done = True

input("Done!" if done else "Error!")

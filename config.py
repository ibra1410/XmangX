import json
import os

import requests
from database import get_db_general_rtb
from utils import get_restarted

super_sudoers = [7304678803]


####################################################################################

# start

wr = get_restarted()
if wr is None:
    if os.path.exists('info.json'):
        fileSize = os.path.getsize("info.json")
        if fileSize == 0:
            
            tokenBot = '7922139743:AAFTj4PwyuR3Ni81cnHDqOFDRs3DBZD3hl8' 
            
            idSudo = 7304678803

            aDict = {"Token": tokenBot, "idSudo": int(idSudo)}
            jsonString = json.dumps(aDict)
            jsonFile = open("info.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close()
    else:
        
        tokenBot = '7922139743:AAFTj4PwyuR3Ni81cnHDqOFDRs3DBZD3hl8'
        
        idSudo = 7304678803

        aDict = {"Token": tokenBot, "idSudo": int(idSudo)}
        jsonString = json.dumps(aDict)
        jsonFile = open("info.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

####################################################################################

# Bot token from Bot Father

# TOKEN = "6440646584:AAH_4iRhExEYh4wbeQBFgj18D-Tve8G0A5M"
f = open('info.json', )
data = json.load(f)
TOKEN = data['Token']


# Your API ID and Hash from https://my.telegram.org/apps
API_ID = 12962251
API_HASH = "b51499523800add51e4530c6f552dbc8"

# Chat used for logs
log_chat = 7304678803
# Sudoers and super sudoers
sudoers = [data['idSudo']]
sudoers += super_sudoers
developer = []
developer += sudoers
f.close()


####################################################################################

def dev():
    lang = get_db_general_rtb("developer")
    lang2 = get_db_general_rtb("secdeveloper")
    if lang is None:
        print("No Developer")
    else:
        for row in lang:
            t = row[0]
            developer.append(t)
    if lang2 is None:
        print("No Second Devoloper")
    else:
        for row in lang2:
            t = row[0]
            developer.append(t)
    print(developer)


def get_bot_information():
    bot_inf = requests.get(
        "https://api.telegram.org/bot" + TOKEN + "/getme")
    bot_info = bot_inf.json()
    result = bot_info["result"]
    bot_id = result["id"]
    bot_username = result["username"]
    return bot_id, bot_username


#####################################################################################


# Prefixes for commands, e.g: /command and !command
prefix = ["/", "!"]

# List of disabled plugins
disabled_plugins = []

# API keys
TENOR_API_KEY = "2MAL8NKBOO01"

# Bot version, do not touch this
with open("version.txt") as f:
    version = f.read().strip()


# Run function
dev()

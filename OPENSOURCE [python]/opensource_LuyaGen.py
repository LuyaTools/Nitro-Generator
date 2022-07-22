#Made by LUYA (ghxstfxce)
#Please dont claim it as yours <3
#Github: https://github.com/LuyaTools
#Telegram: https://t.me/bladetools
#Donate: https://ko-fi.com/luyadevs

#  [!]  Educational purposes only


#the webhook sending version is in the non-sourcecode version <3
# ^^^^^^ READ THIS ^^^^^^ READ THIS ^^^^^^ READ THIS ^^^^^^

import os
import time
from time import sleep
from colorama import init
init()
from colorama import Fore
import requests  #code checking libary
import random
import string
import sys
def repeat():
    os.system('cls')
    amt = input(" Amount: ")
    os.system('cls')         #clears console
    for i in range(int(amt)):      #repeats the generator & checker for the selected amount
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
        if r.status_code == 200:
            print(Fore.GREEN + f"  [+]Valid Nitro Code > discord.gift/{code} - {i}")
                      #the webhook sending version is in the non-sourcecode version <3
        else:
            print(Fore.RED + f"  [!] Invalid > discord.gift/{code}  -  {i}")  
    ext11 = input("\nPress ENTER to exit > ") #exit
    if ext11 == "":
        sys.exit()
    else:
        print(Fore.WHITE + "")
        repeat()
repeat()

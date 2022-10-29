import time
from time import sleep
from colorama import init
init()
from colorama import Fore
import requests  #code checking libary
import random
import string

def clear():
    os.system("cls")

def main():
    clear()
    amt = input("[#] Amount: ")
    clear()
    for z in range(int(amt)):
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
        if r.status_code == 200:
            print(Fore.GREEN + f"  [+] Valid Nitro Code > discord.gift/{code} | Tries: {z}")
            time.sleep(4)
            input()
        else:
            print(Fore.RED + f"  [-] Invalid > discord.gift/{code} | Tries: {z}")
    main()
main()
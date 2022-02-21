import requests
import json 
import time
import colorama
from colorama import Fore

colorama.init()
print(Fore.CYAN)
print('''
________                        .__           __________        __                      
\_____  \   _____   ____   ____ |  |   ____   \______   \ _____/  |_                    
 /   |   \ /     \_/ __ \ / ___\|  | _/ __ \   |    |  _//  _ \   __\                   
/    |    \  Y Y  \  ___// /_/  >  |_\  ___/   |    |   (  <_> )  |                     
\_______  /__|_|  /\___  >___  /|____/\___  >  |______  /\____/|__|                     
        \/      \/     \/_____/           \/          \/                                

                        created by hinick#5819
''')
print(Fore.BLUE)
message = input("Enter Message: ")
timer = int(input("Input Timer Between Messages (3 Seconds Recommended): "))
while True:
    r = requests.post("https://front36.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=XX4XMCHK&topics=%5B%22dreamsmp%22%2C%22tommyinnit%22%2C%22dream%22%2C%22minecraft%22%2C%22fortnite%22%2C%22gaming%22%2C%22anime%22%2C%22manga%22%2C%22discord%22%2C%22twitter%22%2C%22quackity%22%2C%22sapnap%22%2C%22friends%22%2C%22furry%22%5D&lang=en")
    response = r.json()
    print("id obtained, connecting to a chat")
    print("-----------------------------------")
    
    def dostuff(shard):

        dato = {'msg': message, 'id': shard}

        rr = requests.post("https://front44.omegle.com/send", data=dato)

        if rr.status_code == 200:
            print(f"sent {Fore.CYAN}{message}{Fore.BLUE}")
            print("-----------------------------------")
        else:
            print(f"failed to send {message}")
            print("-----------------------------------")
        dataa = {'id': shard}
        disconnecting = requests.post("https://front8.omegle.com/disconnect", data=dataa)
        if disconnecting.status_code == 200:
            print("disconnected")
            print(f"sleeping for {timer} second(s)... ")
            time.sleep(timer)
            print("-----------------------------------")
        else:
            print("failed to disconnect")
        

    def getid():
        shard = response["clientID"]
        if shard.startswith("central"):
            dataa = {'id': shard}
            check = requests.post("https://front8.omegle.com/events", data=dataa)
            print("connected to user, printing event response")
            print("-----------------------------------")
            print(check.text)
            print("-----------------------------------")
            dostuff(shard)

    getid()
